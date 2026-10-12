# Procedure: /update-semester

The student wants to update their course folder. Most downloaded it as a ZIP and have no Git; the script handles both ZIP folders and Git clones. You do everything and explain the result in plain words.

1. Run exactly this command in the course folder: `python .opencode/scripts/update_course.py`. If `python` is not found (typical on macOS), use `python3`; on Windows `py` also works. Do not run any Git or pip command yourself; the script does all of it.
2. Read the output and explain it briefly in the student's language:
   - Was anything new? Name new challenge folders in `my-code/` and what they are for.
   - If course files had been changed or added outside `my-code/`, say calmly that they were reset because course files are read-only, and that their own files belong in `my-code/`.
   - If Git commits had been made in the folder, say that this is not allowed here, that they were removed, and that students never need to commit in this folder.
   - If a template was improved, explain that the script left their copy in `my-code/` alone on purpose, because it is their work. Then follow the section "Template changes" below for that challenge: find out whether their copy still has the old version and offer to bring the change in.
   - If `lifi_hardware` was installed or updated, say so in one sentence.
3. Then read `course/NOW.md` and tell the student in two or three sentences where the semester stands now and what comes next.
4. If the script reports a PROBLEM, follow its WHAT TO DO line and help the student step by step. Never try to repair the folder with Git commands of your own.

## Template changes

When a template changes after students have copied it, the change is described here. For each change: check the student's copy in `my-code/`, and only if it still has the old version, explain in two sentences what is new and ask whether you may bring it in. Change their file only after they agree, and only the part named here; their own code in all other places stays exactly as it is. Afterwards show what you changed and let them run it. Never fill in a `TODO` for them while doing this: the task is theirs.

### challenge-0, 12 October 2026: task 4 "Measure"

What is new: task 4 used to take twenty readings by itself and left nothing to write. Now it takes one reading per Enter (q and Enter stops), the student writes the reading themselves (`r, g, b, c = sensor.read()` and printing the four values), and measures in at least four situations: room light, sensor covered with the hand, phone torch from far away, phone torch close up. Task 5 picks its threshold between "covered" and "torch".

How to recognise the old version: in `my-code/challenge-0/tasks.py`, the function `task_4_read_sensor` contains `for i in range(20):` and no `input()`.

What to change, after the student agrees:

1. In `my-code/challenge-0/tasks.py`, replace the block from the comment line `# Task 4: Measure` down to the end of the function `task_4_read_sensor` with the same block from `course/templates/challenge-0/tasks.py`, including its `TODO`.
2. In task 5 of their file, replace only the comment sentence about finding the threshold and the comment after `threshold = ` with the ones from the template. Keep the student's threshold value and all of their code.
3. Replace `my-code/challenge-0/README.md` with `course/templates/challenge-0/README.md`, unless the student has written something of their own into it; then show them the two changed passages instead.

If the student has already rewritten task 4 in their own way, show them the new version and let them decide; do not overwrite it.
