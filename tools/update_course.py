"""Bring this course folder up to date with the latest course version.

Run by the /update-semester command in OpenCode, or by hand:

    python tools/update_course.py        (on a Mac: python3)

What it does, in this order:

1. Saves every course file you changed yourself into my-code/_saved/<time>/,
   so nothing you typed is ever lost.
2. Fetches the newest course version and makes the course files match it
   exactly. Your own folder my-code/, your key file openai.key and your
   measurement logs are never touched.
3. Copies templates of newly released challenges into my-code/.
4. Installs or updates the module lifi_hardware if the course needs a newer
   version.

The script only prints plain text, so the assistant can explain the result.
"""

import datetime
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MY_CODE = os.path.join(ROOT, "my-code")
TEMPLATES = os.path.join(ROOT, "templates")
MODULE_SOURCE = os.path.join(ROOT, "course", "software", "lifi-hardware-source.md")
MODULE_URL = "git+https://github.com/winf-hsos/lifi-hardware.git"
BRANCH = "main"


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
             "Install Git as described in step 2 of the installation page, "
             "then close and reopen VS Code.")
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        stop("This folder is not a copy made with 'git clone'.",
             "Clone the course repository again as described in step 5 of "
             "the installation page.")
    if "origin" not in git("remote").split():
        stop("This folder does not know where the course lives online.",
             "Ask your lecturer; the folder may have been copied instead of cloned.")


def save_changed_course_files(stamp):
    """Copy course files the student changed, and files in the way, to my-code/_saved/."""
    # Course files changed since the last update, staged or not
    changed = git("diff", "--name-only", "HEAD").splitlines()
    saved = [p for p in changed if p and os.path.isfile(os.path.join(ROOT, p))]
    # Files the student created that the new course version also contains
    incoming = set(git("ls-tree", "-r", "--name-only", f"origin/{BRANCH}").splitlines())
    own = git("ls-files", "--others", "--exclude-standard").splitlines()
    saved += [p for p in own if p in incoming]
    if not saved:
        return []
    target = os.path.join(MY_CODE, "_saved", stamp)
    for path in saved:
        dest = os.path.join(target, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(os.path.join(ROOT, path), dest)
    return saved


def copy_new_templates(changed_paths):
    """Copy released templates into my-code/; never overwrite what is there."""
    added, updated = [], []
    # Only templates that are part of the course, not folders a student made
    released = git("ls-tree", "-d", "--name-only", "HEAD", "templates/", check=False)
    names = [line.split("/", 1)[1] for line in released.splitlines() if "/" in line]
    if not names:
        return added, updated
    os.makedirs(MY_CODE, exist_ok=True)
    for name in sorted(names):
        source = os.path.join(TEMPLATES, name)
        if not os.path.isdir(source):
            continue
        target = os.path.join(MY_CODE, name)
        if not os.path.exists(target):
            shutil.copytree(source, target,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            added.append(name)
        elif any(p.startswith(f"templates/{name}/") for p in changed_paths):
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
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    saved = save_changed_course_files(stamp)

    # Commits made in this folder by hand are kept on a side branch
    own_commits = git("rev-list", f"origin/{BRANCH}..HEAD", check=False)
    if own_commits:
        git("branch", f"saved-{stamp}", "HEAD", check=False)

    changed_paths = []
    if before != after:
        changed_paths = git("diff", "--name-only", before, after, check=False).splitlines()
    git("reset", "--quiet", "--hard", f"origin/{BRANCH}")

    added, updated = copy_new_templates(changed_paths)
    module = update_module()

    say()
    say("RESULT")
    if before == after and not saved:
        say("- Your course folder was already up to date.")
    else:
        say(f"- Course folder updated ({len(changed_paths)} course files changed).")
    if saved:
        say(f"- You had changed {len(saved)} course file(s). Your versions are saved in "
            f"my-code/_saved/{stamp}/ :")
        for path in saved:
            say(f"    {path}")
    if own_commits:
        say(f"- Your own Git commits are kept on the branch saved-{stamp}.")
    for name in added:
        say(f"- NEW: my-code/{name}/ is ready for you to work in.")
    for name in updated:
        say(f"- The template templates/{name}/ was improved. Your copy in my-code/{name}/ "
            f"was NOT changed; compare the two if you want the improvements.")
    say(f"- {module}")
    now = os.path.join(ROOT, "NOW.md")
    if os.path.isfile(now):
        with open(now, encoding="utf-8") as f:
            for line in f:
                if line.startswith("Updated:"):
                    say(f"- NOW.md: {line.strip()}")
                    break


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        say(f"PROBLEM: {error}")
        say("WHAT TO DO: Show this message to your assistant or your lecturer.")
        sys.exit(1)
