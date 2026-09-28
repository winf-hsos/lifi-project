# Where the semester stands

Updated: 2026-09-28, week 1

## Current

- **Session 1 (28 September) took place: getting set up.** The devices were not handed out yet. In the session everyone installed OpenCode Desktop, downloaded this course folder as a ZIP, ran `/onboarding` (the device test is skipped until the devices arrive) and opened the course folder in VS Code. That is as far as the session got. Whoever did not finish, completes the setup at home with `/onboarding`.
- **Open exercise, not done in class yet: a countdown timer with a coloured lamp in the terminal.** It was planned for session 1 but there was no time left; it comes briefly at the start of session 2. Students may start it at home already, and you help them if they ask; do not treat it as done. The student creates `my-code/timer.py` in VS Code. The "lamp" is a small function `lamp(r, g, b)` that prints a coloured block in the terminal, with r, g and b from 0 to 255, exactly like the LED later (`[48;2;r;g;bm` plus spaces plus `[0m`; you may write this function for them and explain it if they ask). Five steps, one at a time, exactly as on the slides of "first light" (part "your first program"): (1) ask how many seconds with `input()` and turn the text into a number with `int()`; typing "five" crashes with a `ValueError`, which is the error message the class reads together; (2) check the input with `while not text.isdigit():` and ask again; (3) count down with `for remaining in range(seconds, 0, -1):`, `print(remaining, "s")` and `time.sleep(1)`, then print "time is up!"; (4) the function `lamp(r, g, b)` (on the slides: `on = f"[48;2;{r};{g};{b}m"`, `off = "[0m"`, `print(on + " " * 12 + off, end=" ")`); (5) `if remaining <= 5:` yellow, `else:` green, and after the loop one red lamp. The slides show every step as code with a copy button, so students may paste it; your job is that they understand each line, not to produce it. Let them decide what happens when someone types "five" instead of 5. Go step by step, let them run and change each step themselves, and do not hand over the whole program at once. Next week they replace `lamp` with `led.set_color` and the timer runs on the device.
- **If the lamp shows strange characters instead of colours** (something like `←[48;2;0;200;0m` or `[48;2;0;200;0m`), the program runs in a console that does not switch colour codes on by itself, usually the old Windows `cmd.exe` or a Python window started by double-click. Solve it together with the student, do not just fix it silently: first ask where they started the program and what exactly they see, then explain in one or two sentences what the codes are (instructions to the terminal, not text). Two fixes, both fine: run the program in the terminal of VS Code, or add `import os` and `os.system("")` at the top of the program, which switches colour codes on in the Windows console.
- **Until next Monday: form teams of two.** Next Monday every team of two gets its two devices, one per person. If a student has no partner yet, they tell Nicolas.
- **Next: the devices, then Challenge 0 ("The Spark").** First own lines of code: switch the LED on, blink, change colours, read the sensor, react to a reading. The template is released: the student works in `my-code/challenge-0/`.

## Covered so far

- What the module is about, the device, the five challenges.
- You are the receiver: an experiment in which the projector flashed colours and the class wrote them down, and found out what a receiver has to manage (too many colours to tell apart, too fast so a repeated colour gets lost, where does the message start, did everything arrive).

## Not open yet

- The standardisation session has **not** taken place. There is no class standard for the frame format yet. See "What you do not give away" in your instructions.

## Fixed values

- Language model: for now the course uses OpenCode's free models, preset in the course folder. A key for a stronger model may follow; Nicolas announces it.

- Distance between the two devices: **not yet fixed**, will be measured and announced.

## The exam

- A one-hour multiple-choice exam on the concepts, everybody on their own. The date is set by the university and announced in ILIAS.
- If all five challenges (0 to 4) are accepted, the student gets a 5 % bonus on the exam: all or nothing. What counts is the passed acceptance test with its live change. Documentation is optional and only for the team; the one exception is the protocol specification in Challenge 3, which another team needs in the interop test.
- The ranking in the competitions does not count towards the grade.

## The fourteen sessions (winter term 2026/27, Mondays 15:00 to 18:15, room HD0001)

Each session carries a concept as its title; what happens in the project follows after the colon.

1. 28.09. Kick-off: overview and setup: kits, setup, Challenge 0 starts
2. 05.10. Cutting Problems, Algorithms and Programs: Challenge 0, your first program
3. 12.10. Measuring and Experimenting: Challenge 0 is checked
4. 19.10. Analog and Digital, Symbols and Information: Challenge 1 starts
   (26.10. excursion week, no session)
5. 02.11. Signal and Noise: competition, Challenge 1 (The Alphabet)
6. 09.11. Number Systems and Code Systems: Challenge 2 starts
7. 16.11. Sampling and Synchronization: Challenge 2, faster
8. 23.11. Throughput and Limits: competition, Challenge 2 (The Word)
9. 30.11. Protocols: Challenge 3 starts
10. 07.12. Logic and Arithmetic: interop test
11. 14.12. Memory and Storage: competition, Challenge 3 (The Listener)
12. 21.12. Errors and Redundancy: standardisation session, Challenge 4 starts
    (28.12. Christmas break, no session)
13. 04.01. Compression: Challenge 4, faster and shorter
14. 11.01. Abstraction and Layers: final, Challenge 4 (The Packet)

The schedule in ILIAS is the binding version; changes are announced there.
