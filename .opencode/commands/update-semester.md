---
description: Bring this course folder up to date (new material, templates, NOW.md, lifi_hardware)
---

The student wants to update their course folder. Most downloaded it as a ZIP and have no Git; the script handles both ZIP folders and Git clones. You do everything and explain the result in plain words.

1. Run exactly this command in the course folder: `python .opencode/scripts/update_course.py`. If `python` is not found (typical on macOS), use `python3`; on Windows `py` also works. Do not run any Git or pip command yourself; the script does all of it.
2. Read the output and explain it briefly in the student's language:
   - Was anything new? Name new challenge folders in `my-code/` and what they are for.
   - If course files had been changed or added outside `my-code/`, say calmly that they were reset because course files are read-only, and that their own files belong in `my-code/`.
   - If Git commits had been made in the folder, say that this is not allowed here, that they were removed, and that students never need to commit in this folder.
   - If a template was improved, explain that their copy in `my-code/` was left alone on purpose, and offer to show the differences.
   - If `lifi_hardware` was installed or updated, say so in one sentence.
3. Then read `course/NOW.md` and tell the student in two or three sentences where the semester stands now and what comes next.
4. If the script reports a PROBLEM, follow its WHAT TO DO line and help the student step by step. Never try to repair the folder with Git commands of your own.
