"""Bring this course folder up to date with the latest course version.

Run by the /update-semester command in OpenCode:

    python .opencode/scripts/update_course.py        (on a Mac: python3)

Works for both ways of getting the course folder:

- downloaded as ZIP (the standard way): the newest ZIP is downloaded and
  unpacked over the folder. No Git needed.
- cloned with Git (the alternative): the folder is reset to the newest
  version with Git.

Rules of the course folder, the same for both ways:

- my-code/ belongs to the student. Nothing in it is ever changed or deleted.
- Everything else belongs to the course and is read-only for students.
  Changed course files are overwritten, extra files inside course/ are
  removed, and in a Git clone commits made by the student are removed.
- Templates of newly released challenges are copied into my-code/.
- lifi_hardware is installed or updated if the course needs a newer version.

The output is plain text, so the assistant can explain the result.
"""

import hashlib
import io
import os
import re
import shutil
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MY_CODE = os.path.join(ROOT, "my-code")
TEMPLATES = os.path.join(ROOT, "course", "templates")
NOW = os.path.join(ROOT, "course", "NOW.md")
MODULE_SOURCE = os.path.join(ROOT, "course", "material", "software", "lifi-hardware-source.md")
MODULE_ZIP = "https://github.com/winf-hsos/lifi-hardware/archive/refs/heads/main.zip"
COURSE_ZIP = os.environ.get("LIFI_COURSE_ZIP",
                            "https://github.com/winf-hsos/lifi-project/archive/refs/heads/main.zip")
BRANCH = "main"
# Folders that belong to the course completely; files there that are not part
# of the course are removed. .opencode/ is not in this list because OpenCode
# keeps its own files in it.
COURSE_ONLY = ["course"]
COURSE_ONLY_OPENCODE = [".opencode/commands", ".opencode/scripts"]


def say(text=""):
    print(text, flush=True)


def stop(problem, advice):
    say(f"PROBLEM: {problem}")
    say(f"WHAT TO DO: {advice}")
    say("Nothing in your folder was changed.")
    sys.exit(1)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def is_student_area(path):
    return path == "my-code" or path.startswith("my-code/")


# --- downloading ---------------------------------------------------------------

def ssl_context():
    """The normal certificates, or pip's own if Python has none (fresh macOS install)."""
    try:
        from pip._vendor import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def download(url):
    if url.startswith("file:"):
        with urllib.request.urlopen(url) as response:
            return response.read()
    try:
        with urllib.request.urlopen(url, timeout=60, context=ssl.create_default_context()) as r:
            return r.read()
    except (ssl.SSLError, urllib.error.URLError) as error:
        if "CERTIFICATE" not in str(error).upper():
            raise
        with urllib.request.urlopen(url, timeout=60, context=ssl_context()) as r:
            return r.read()


# --- the ZIP way ---------------------------------------------------------------

def digest(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def update_from_zip():
    """Unpack the newest course ZIP over the folder; returns (changed, removed)."""
    try:
        data = download(COURSE_ZIP)
    except Exception as error:
        stop("The newest course version could not be downloaded.",
             f"Check your internet connection and try again. Details: {error}")
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        stop("The downloaded course version is damaged.", "Try again in a few minutes.")

    incoming = {}
    for name in archive.namelist():
        if name.endswith("/"):
            continue
        inner = name.split("/", 1)[1] if "/" in name else name   # drop "lifi-project-main/"
        if inner and (not is_student_area(inner) or inner == "my-code/README.md"):
            incoming[inner] = name

    changed = []
    for inner, name in sorted(incoming.items()):
        target = os.path.join(ROOT, *inner.split("/"))
        content = archive.read(name)
        if os.path.isfile(target):
            with open(target, "rb") as f:
                if f.read() == content:
                    continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as f:
            f.write(content)
        changed.append(inner)

    removed = []
    for area in COURSE_ONLY + COURSE_ONLY_OPENCODE:
        base = os.path.join(ROOT, *area.split("/"))
        for folder, dirs, files in os.walk(base, topdown=False):
            for file in files:
                path = rel(os.path.join(folder, file))
                if path not in incoming:
                    os.remove(os.path.join(folder, file))
                    removed.append(path)
            if folder != base and not os.listdir(folder):
                os.rmdir(folder)
    known_root = {p for p in incoming if "/" not in p}
    stray = [f for f in os.listdir(ROOT)
             if os.path.isfile(os.path.join(ROOT, f)) and f not in known_root
             and not f.startswith(".") and f != "lifi_log.jsonl"]
    return changed, removed, stray


# --- the Git way ---------------------------------------------------------------

def git(*args, check=True):
    result = subprocess.run(["git", "-c", "core.quotePath=false", "-C", ROOT, *args],
                            capture_output=True, text=True, encoding="utf-8",
                            errors="replace")
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout.rstrip()


def update_from_git():
    """Reset the clone to the newest version; returns (changed, removed, stray, own_commits)."""
    if shutil.which("git") is None:
        stop("This folder was cloned with Git, but Git cannot be found.",
             "Reinstall Git (see the installation page), then restart OpenCode.")
    fetched = subprocess.run(["git", "-C", ROOT, "fetch", "--quiet", "origin", BRANCH],
                             capture_output=True, text=True, errors="replace")
    if fetched.returncode != 0:
        stop("The newest course version could not be downloaded.",
             "Check your internet connection and try again. Details: "
             + fetched.stderr.strip()[-300:])
    before = git("rev-parse", "HEAD")
    own_commits = git("rev-list", f"origin/{BRANCH}..HEAD", check=False).splitlines()
    touched = [p for p in git("diff", "--name-only", "HEAD").splitlines() if p]
    extra = [p for p in git("ls-files", "--others", "--exclude-standard", "--",
                            *COURSE_ONLY, *COURSE_ONLY_OPENCODE).splitlines() if p]
    changed = git("diff", "--name-only", before, f"origin/{BRANCH}", check=False).splitlines()
    git("reset", "--quiet", "--hard", f"origin/{BRANCH}")
    git("clean", "--quiet", "-f", "-d", "--", *COURSE_ONLY, *COURSE_ONLY_OPENCODE)
    stray = [p for p in git("ls-files", "--others", "--exclude-standard").splitlines()
             if p and not is_student_area(p)]
    return [p for p in changed if p], touched + extra, stray, own_commits


# --- after either way ----------------------------------------------------------

def copy_new_templates(changed_paths):
    """Copy released templates into my-code/; never overwrite what is there."""
    added, updated = [], []
    os.makedirs(MY_CODE, exist_ok=True)
    names = sorted(os.listdir(TEMPLATES)) if os.path.isdir(TEMPLATES) else []
    for name in names:
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
                             "--force-reinstall", "--quiet", MODULE_ZIP],
                            capture_output=True, text=True, errors="replace")
    if result.returncode != 0:
        return ("PROBLEM: lifi_hardware could not be installed. pip said:\n"
                + result.stderr.strip()[-1500:])
    return f"lifi_hardware {needed or ''} installed.".replace("  ", " ")


def main():
    say("Updating your course folder ...")
    own_commits = []
    if os.path.isdir(os.path.join(ROOT, ".git")):
        way = "Git"
        changed, reset, stray, own_commits = update_from_git()
        reset_note = reset
    else:
        way = "ZIP"
        changed, removed, stray = update_from_zip()
        reset_note = removed

    added, updated = copy_new_templates(changed)
    module = update_module()

    say()
    say(f"RESULT (course folder from {way})")
    if changed:
        say(f"- New course material: {len(changed)} course file(s) added or changed.")
    else:
        say("- There was no new course material; your course folder is up to date.")
    if own_commits:
        say(f"- NOT ALLOWED: {len(own_commits)} Git commit(s) had been made in this folder. "
            "They were removed. Students do not commit here; your work lives in my-code/.")
    if reset_note:
        say(f"- {len(reset_note)} file(s) outside my-code/ had been changed or added and were "
            "reset. Course files are read-only; put your own files in my-code/.")
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
