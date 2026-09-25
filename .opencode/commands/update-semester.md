---
description: Bring this course folder up to date (new material, templates, NOW.md, lifi_hardware)
---

The student wants to update their course folder. They do not know Git, so you do everything and explain the result in plain words.

1. Run exactly this command in the repository root: `python tools/update_course.py`. If the command `python` is not found (typical on macOS), run `python3 tools/update_course.py` instead. Do not run any other Git or pip command yourself; the script does all of it safely.
2. Read the output and explain it briefly in the student's language:
   - Was anything new? Name new challenge folders in `my-code/` and what they are for.
   - If course files the student had changed were saved to `my-code/_saved/...`, say so calmly: nothing is lost, and their own work belongs in `my-code/`.
   - If a template was improved, explain that their copy in `my-code/` was left alone on purpose, and offer to show the differences.
   - If `lifi_hardware` was installed or updated, say so in one sentence.
3. Then read `NOW.md` again and tell the student in two or three sentences where the semester stands now and what comes next.
4. If the script reports a PROBLEM, follow its WHAT TO DO line and help the student step by step. Never try to repair the folder with Git commands of your own.
