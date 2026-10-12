# Where the semester stands

Updated: 2026-10-12, week 3

## Current

- **Session 3 (Monday 12 October): three inputs and the teams.** The inputs that did not fit into session 2 come now: Cutting Problems, Solving Problems with Computers (the IPO model) and What is a program? (Algorithms and Programs). At the start of the session the teams of two are registered. After the break Nicolas colours the countdown timer with `if` and splits it into functions of its own, live at the visualizer.
- **Challenge 0 ("The Spark") is checked today**, at the seat during the workshop: the team shows its running program (set the LED, read the sensor). Whoever does not finish today shows it in the online session by sharing the screen and pointing the camera at the device.
- **The timer, continued.** The countdown with `for` and `time.sleep` was done in session 2. What follows is colouring it with `if` (yellow in the last five seconds, green before, one red lamp at the end) and moving the lamp and the countdown into functions of their own. Go step by step, let the student run and change each step, and do not hand over the whole program at once. If the terminal shows strange characters such as `←[48;2;0;200;0m` instead of colours, the program runs in a console that does not switch colour codes on by itself: run it in the terminal of VS Code, or add `import os` and `os.system("")` at the top. Explain what the codes are, do not just fix it silently.
- **Session 4 is online: Wednesday 21 October, 13:15 to 16:30, in Teams.** Monday 19 October is cancelled. The link is in ILIAS. Topic: Measuring and Experimenting. Everyone measures with their own device at home, so students need: the device on the laptop with the Brick Daemon running, a white sheet of paper (it reflects the LED back into the sensor), the torch of their phone, a room where the light can be switched off, and a headset.
- **Challenge 0, task 4 is new (12 October):** it now takes one reading per Enter (q stops it), and the student writes the reading themselves: `r, g, b, c = sensor.read()` and print the four values. They measure in at least four situations, changing one thing at a time: room light, sensor covered with the hand, phone torch from far away, phone torch close up, and note the clear value c; the threshold of task 5 goes between "covered" and "torch". A value stuck at 65535 means the sensor is overloaded: torch further away. Students who copied `tasks.py` before 12 October still have the old task 4 (twenty readings, nothing to write); the current version is in `course/templates/challenge-0/tasks.py`. Offer to show them the new task 4, but do not overwrite their file.
- **Until the online session:** finish the sensor tasks of Challenge 0 (print the sensor values continuously, LED and sensor in one program) and read the concept page Measuring and Experimenting.
- **26 October: excursion week, no session.** Session 5 follows on 2 November.
- **New: `lifi_hardware` 0.4.0 lets one laptop drive both devices of a team.** With two devices plugged into the same laptop, each script says which one it means by the UID of its master brick (shown in the Brick Viewer): `from lifi_hardware import led, sensor, use_device`, then `use_device("64SK5w")` before the first use of `led` or `sensor`; after that everything works as before. Without a choice, two plugged-in devices now give an error message that names both UIDs. To get the new version, the student runs `/update-semester`. With one device nothing changes.
- **Practice questions** are on the practice platform, one page per concept, switchable to German. The concept pages link to them.

## Covered so far

- Session 1: what the module is about, the device, the five challenges, and the experiment "you are the receiver" (the projector flashed colours, the class wrote them down and found out what a receiver has to manage). Setup with OpenCode Desktop and `/onboarding`.
- Session 2: checking the setup, the first program `hello.py`, input, variables and data types, the countdown timer with a `for` loop and `sleep`. The devices were handed out and shown in the Brick Viewer; Challenge 0 started.
- Session 3: Cutting Problems, Solving Problems with Computers, What is a program? (taking place today).

## Not open yet

- The standardisation session has **not** taken place. There is no class standard for the frame format yet. See "What you do not give away" in your instructions.

## Fixed values

- Language model: for now the course uses OpenCode's free models, preset in the course folder. A key for a stronger model may follow; Nicolas announces it.

- Distance between the two devices: **not yet fixed**, will be measured and announced.

## The exam

- A one-hour multiple-choice exam on the concepts, everybody on their own. Nicolas announced Friday 5 February 2027; the date is not confirmed yet and will be announced in ILIAS.
- If all five challenges (0 to 4) are accepted, the student gets a 5 % bonus on the exam: all or nothing. What counts is the passed acceptance test with its live change. Documentation is optional and only for the team; the one exception is the protocol specification in Challenge 3, which another team needs in the interop test.
- The ranking in the competitions does not count towards the grade.

## The fourteen sessions (winter term 2026/27, Mondays 15:00 to 18:15, room HD0001)

Each session carries a concept as its title; what happens in the project follows after the colon. Since 12 October all topics and competitions have moved back by one session, and Abstraction and Layers no longer has an input of its own.

1. 28.09. Kick-off: overview and setup: kits, setup, Challenge 0 starts
2. 05.10. Setup and first programs: devices handed out, Challenge 0
3. 12.10. Solving Problems, Cutting Problems, Algorithms and Programs: teams registered, Challenge 0 is checked
4. **Wednesday 21.10., 13:15 to 16:30, online in Teams.** Measuring and Experimenting: the sensor
   (26.10. excursion week, no session)
5. 02.11. Analog and Digital, Symbols and Information: Challenge 1 starts
6. 09.11. Signal and Noise: competition, Challenge 1 (The Alphabet)
7. 16.11. Number Systems and Code Systems: Challenge 2 starts
8. 23.11. Sampling and Synchronization: Challenge 2, faster
9. 30.11. Throughput and Limits: competition, Challenge 2 (The Word)
10. 07.12. Protocols: Challenge 3 starts
11. 14.12. Logic and Arithmetic: interop test
12. 21.12. Memory and Storage: competition, Challenge 3 (The Listener), then the standardisation session; Challenge 4 starts
    (28.12. Christmas break, no session)
13. 04.01. Errors and Redundancy: Challenge 4, the class standard runs
14. 11.01. Compression: final, Challenge 4 (The Packet)

The schedule in ILIAS is the binding version; changes are announced there.
