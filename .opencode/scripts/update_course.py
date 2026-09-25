"""Bring this course folder up to date with the latest course version.

Run by the /update-semester command in OpenCode:

    python .opencode/scripts/update_course.py        (on a Mac: python3)

Rules of the course folder:

- my-code/ belongs to the student. This script never changes or deletes
  anything in it, and neither does it touch openai.key.
- Everything else belongs to the course and is read-only for students.
  The script makes it match the newest course version exactly: changed
  course files are overwritten, extra files inside course/ and .opencode/
  are removed, and Git commits made in this folder are removed (students
  do not commit here).
- Templates of newly released challenges are copied into my-code/.
- lifi_hardware is installed or updated if the course needs a newer version.

The output is plain text, so the assistant can explain the result.
"""

import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MY_CODE = os.path.join(ROOT, "my-code")
TEMPLATES = os.path.join(ROOT, "course", "templates")
NOW = os.path.join(ROOT, "course", "NOW.md")
MODULE_SOURCE = os.path.join(ROOT, "course", "material", "software", "lifi-hardware-source.md")
MODULE_URL = "git+https://github.com/winf-hsos/lifi-hardware.git"
BRANCH = "main"
COURSE_PATHS = ["course", ".opencode"]   # read-only areas that are cleaned completely


def say(text=""):
    print(text, flush=True)


def git(*args, check=True):
    """Run git in the course folder and return its output as text."""
    result = subprocess.run(["git", "-c", "core.quotePath=false", "-C", ROOT, *args],
                            capture_output=True, text=True, encoding="utf-8",
                            errors="replace")
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout.rstrip()


def stop(problem, advice):
    say(f"PROBLEM: {problem}")
    say(f"WHAT TO DO: {advice}")
    say("Nothing in your folder was changed.")
    sys.exit(1)


def check_preconditions():
    if shutil.which("git") is None:
        stop("Git is not installed or cannot be found.",
             "Install Git (see the installation page), then close and reopen VS Code.")
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        stop("This folder is not a copy made with 'git clone'.",
             "Clone the course repository again as described on the installation page.")
    if "origin" not in git("remote").split():
        stop("This folder does not know where the course lives online.",
             "Ask your lecturer; the folder may have been copied instead of cloned.")


def copy_new_templates(changed_paths):
    """Copy released templates into my-code/; never overwrite what is there."""
    added, updated = [], []
    released = git("ls-tree", "-d", "--name-only", "HEAD", "course/templates/", check=False)
    names = [line.rsplit("/", 1)[1] for line in released.splitlines() if "/" in line]
    os.makedirs(MY_CODE, exist_ok=True)
    for name in sorted(names):
        source = os.path.join(TEMPLATES, name)
        target = os.path.join(MY_CODE, name)
        if not os.path.isdir(source):
            continue
        if not os.path.exists(target):
            shutil.copytree(source, target,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            added.append(name)
        elif any(p.startswith(f"course/templates/{name}/") for p in changed_paths):
            updated.append(name)
    return added, updated


def version_tuple(text):
    return tuple(int(x) for x in re.findall(r"\d+", text)[:3])


def update_module():
    """Install lifi_hardware, or update it if the course needs a newer version."""
    needed = None
    try:
        with open(MODULE_SOURCE, encoding="utf-8") as f:
            m = re.search(r"`lifi_hardware` (\d+\.\d+\.\d+)", f.readline())
            needed = m.group(1) if m else None
    except OSError:
        pass
    try:
        from importlib.metadata import version, PackageNotFoundError
        try:
            installed = version("lifi-hardware")
        except PackageNotFoundError:
            installed = None
    except ImportError:
        installed = None

    if installed and needed and version_tuple(installed) >= version_tuple(needed):
        return f"lifi_hardware {installed} is installed, that is the current version."
    what = "Updating" if installed else "Installing"
    say(f"{what} lifi_hardware (this can take a minute) ...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade",
                             "--force-reinstall", "--quiet", MODULE_URL],
                            capture_output=True, text=True, errors="replace")
    if result.returncode != 0:
        return ("PROBLEM: lifi_hardware could not be installed. pip said:\n"
                + result.stderr.strip()[-1500:])
    return f"lifi_hardware {needed or ''} installed.".replace("  ", " ")


def main():
    say("Updating your course folder ...")
    check_preconditions()

    fetched = subprocess.run(["git", "-C", ROOT, "fetch", "--quiet", "origin", BRANCH],
                             capture_output=True, text=True, errors="replace")
    if fetched.returncode != 0:
        stop("The newest course version could not be downloaded.",
             "Check your internet connection and try again. Details: "
             + fetched.stderr.strip()[-300:])

    before = git("rev-parse", "HEAD")
    after = git("rev-parse", f"origin/{BRANCH}")
    own_commits = git("rev-list", f"origin/{BRANCH}..HEAD", check=False).splitlines()
    touched = [p for p in git("diff", "--name-only", "HEAD").splitlines() if p]
    extra = [p for p in git("ls-files", "--others", "--exclude-standard", "--",
                            *COURSE_PATHS).splitlines() if p]

    changed_paths = []
    if before != after:
        changed_paths = git("diff", "--name-only", before, after, check=False).splitlines()
    git("reset", "--quiet", "--hard", f"origin/{BRANCH}")
    git("clean", "--quiet", "-f", "-d", "--", *COURSE_PATHS)

    added, updated = copy_new_templates(changed_paths)
    module = update_module()

    say()
    say("RESULT")
    if before == after and not own_commits:
        say("- There was no new course material; your course folder is up to date.")
    else:
        new = len([p for p in changed_paths if p])
        say(f"- New course material: {new} course file(s) added or changed.")
    if own_commits:
        say(f"- NOT ALLOWED: {len(own_commits)} Git commit(s) had been made in this folder. "
            "They were removed. Students do not commit here; your work lives in my-code/.")
    if touched or extra:
        say(f"- {len(touched) + len(extra)} course file(s) had been changed or added outside "
            "my-code/ and were reset. Course files are read-only; put your own files in my-code/.")
    stray = [p for p in git("ls-files", "--others", "--exclude-standard").splitlines()
             if p and not p.startswith("my-code/")]
    if stray:
        say(f"- These files of yours are outside my-code/: {', '.join(stray)}. "
            "They were left alone, but please move them into my-code/.")
    for name in added:
        say(f"- NEW: my-code/{name}/ is ready for you to work in.")
    for name in updated:
        say(f"- The template course/templates/{name}/ was improved. Your copy in my-code/{name}/ "
            f"was NOT changed; compare the two if you want the improvements.")
    say(f"- {module}")
    if os.path.isfile(NOW):
        with open(NOW, encoding="utf-8") as f:
            for line in f:
                if line.startswith("Updated:"):
                    say(f"- course/NOW.md: {line.strip()}")
                    break


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        say(f"PROBLEM: {error}")
        say("WHAT TO DO: Show this message to your assistant or your lecturer.")
        sys.exit(1)
