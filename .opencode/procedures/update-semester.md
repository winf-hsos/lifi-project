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

### challenge-0, 12 October 2026: one file per task, and a new task 4

What is new: the six tasks of Challenge 0 used to be functions in one file, `tasks.py`. Now every task is a script of its own (`task_1_light_on.py` to `task_6_human_receiver.py`), run with `python task_3_color_cycle.py` and so on. Comments are written with `#` only. Task 4 changed as well: it takes one reading per Enter (q and Enter stops), the student writes the reading themselves (`r, g, b, c = sensor.read()` and printing the four values), and measures in at least four situations: room light, sensor covered with the hand, phone torch from far away, phone torch close up. Task 5 picks its threshold between "covered" and "torch".

How to recognise the old version: `my-code/challenge-0/tasks.py` exists.

What happens by itself: the update script adds the six new files to `my-code/challenge-0/` next to `tasks.py` and changes nothing that is already there. If the new files are missing after `/update-semester`, run `python .opencode/scripts/update_course.py` once more: the first run still used the previous version of the script, which did not add files to an existing folder.

What to offer, and do only after the student agrees:

1. For every task they have already solved in `tasks.py`, carry their own lines over into the matching new file, in place of its `TODO` lines. Their code moves as it is; do not improve it on the way, and do not fill in a task they have not solved yet.
2. Task 4 has nothing to carry over, because the old task 4 had nothing to write; the new file stays as it is, with its `TODO`.
3. In task 5, carry over their threshold value and their condition.
4. Run each file they have solved once, so they see it still works.
5. `tasks.py` can stay as a record of their work. Tell them they may delete it themselves once the new files run.
6. `my-code/challenge-0/README.md` still describes `tasks.py`. Replace it with `course/templates/challenge-0/README.md`, unless the student has written something of their own into it; then only point them to the new one.

If the student does not want any of this, leave everything as it is: the new files are there to work in whenever they like.
