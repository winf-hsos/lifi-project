# Where the semester stands

Updated: 2026-09-28, week 1

## Current

- **Session 1 (28 September): getting set up, and a first program without the device.** The devices are handed out later, not today. Everyone installs OpenCode Desktop, downloads this course folder as a ZIP and runs `/onboarding`, which walks them through the remaining installations; the device test is skipped for now.
- **Today's first program, in pairs: a countdown timer with a coloured lamp in the terminal.** The student creates `my-code/timer.py` in VS Code. The "lamp" is a small function `lamp(r, g, b)` that prints a coloured block in the terminal, with r, g and b from 0 to 255, exactly like the LED later (`[48;2;r;g;bm` plus spaces plus `[0m`; you may write this function for them and explain it if they ask). Four steps, one at a time: (1) ask how many seconds and print them; `input()` gives text, so adding 1 fails until they use `int()`, which is a good error to read together; (2) count down one line per second with a loop and `time.sleep(1)`; (3) a green lamp while it runs, red at the end; (4) yellow for the last five seconds and blink red three times at the end. Let them decide what happens when someone types "five" instead of 5. Go step by step, let them run and change each step themselves, and do not hand over the whole program at once. Next week they replace `lamp` with `led.set_color` and the timer runs on the device.
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
