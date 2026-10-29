# Where the semester stands

Updated: 2026-10-29, excursion week

## Current

- **Update before Monday 2 November: run `/update-semester`.** The course server has moved to a new address, `lifi.hsos.uber.space`; the old address stops working at the end of October. `lifi_hardware` 0.4.3 sends the measurement log to the new server, and `/update-semester` installs it. Older versions keep working on the device, but the live view in the team cockpit and the challenge tests then see nothing. If a student's cockpit stays empty, ask which version they have (`python -c "import lifi_hardware; print(lifi_hardware.__version__)"`) and run `/update-semester`.
- **New addresses:** team cockpit https://lifi.hsos.uber.space/cockpit, practice questions https://live.hsos.uber.space/practice/dup-ws2026, anonymous feedback https://live.hsos.uber.space/feedback/dup-ws2026, live polls in the sessions https://live.hsos.uber.space/q. The old `lifi.uber.space` links forward only until the end of October.
- **No sessions on 19 and 26 October.** 19 October was cancelled, 26 October is the excursion week. Session 4 is on Monday 2 November in HD0001, session 5 is the replacement for 19 October: **Wednesday 4 November, 09:45 to 13:00, online in Teams** (link in ILIAS).
- **Challenge 0 has no acceptance test** (Nicolas, 12 October). It is practice: tasks 1 to 3 were done in session 3, tasks 4 to 6 (the sensor) were homework. Help students who are still on them.
- **Challenge 1 ("The Alphabet") starts in session 4**, and its competition is in session 6 on 9 November.
- **Language model:** since session 3 everyone has a shared OpenAI key from ILIAS, because the free models failed during the session. The student enters it in OpenCode (Settings, Providers, OpenAI) and chooses the course model in the model selection below the input field. Never ask for the key and never print it.
- **Challenge 0 has one file per task:** `task_1_light_on.py` to `task_6_human_receiver.py` in `my-code/challenge-0/`, each run on its own (`python task_4_measure.py`). Task 4 takes one reading per Enter (q stops); the student writes the reading themselves (`r, g, b, c = sensor.read()` and print the four values) and measures in at least four situations: room light, sensor covered with the hand, phone torch from far away, phone torch close up; the threshold of task 5 goes between "covered" and "torch". A value stuck at 65535 means the sensor is overloaded: torch further away. Students who started before 12 October may still have `my-code/challenge-0/tasks.py`; then follow the section "Template changes" of `.opencode/procedures/update-semester.md`, only with their consent.
- **Two devices on one laptop:** with `lifi_hardware` 0.4.0 or newer each script says which device it means: `from lifi_hardware import led, sensor, use_device`, then `use_device("<UID of the master brick>")` before the first use of `led` or `sensor`. The UID is shown in the Brick Viewer.
- **Practice questions** are on the practice platform, one page per concept, switchable to German. The concept pages link to them.

## Covered so far

- Session 1: what the module is about, the device, the five challenges, and the experiment "you are the receiver". Setup with OpenCode Desktop and `/onboarding`.
- Session 2: checking the setup, the first program `hello.py`, input, variables and data types, the countdown timer with a `for` loop and `sleep`. The devices were handed out; Challenge 0 started.
- Session 3: Cutting Problems and Solving Problems with Computers (the IPO model), Challenge 0 tasks 1 to 3 with discussion. What is a program? (Algorithms and Programs) did not fit and follows in session 4.

## Not open yet

- The standardisation session has **not** taken place. There is no class standard for the frame format yet. See "What you do not give away" in your instructions.

## Fixed values

- Language model: the shared OpenAI key from ILIAS with the course model; OpenCode's free models remain a fallback.

- Distance between the two devices: **not yet fixed**, will be measured and announced.

## The exam

- A one-hour multiple-choice exam on the concepts, everybody on their own. Nicolas announced Friday 5 February 2027; the date is not confirmed yet and will be announced in ILIAS.
- If all five challenges (0 to 4) are accepted, the student gets a 5 % bonus on the exam: all or nothing. What counts is the passed acceptance test with its live change. Documentation is optional and only for the team; the one exception is the protocol specification in Challenge 3, which another team needs in the interop test.
- The ranking in the competitions does not count towards the grade.

## The fourteen sessions (winter term 2026/27, Mondays 15:00 to 18:15, room HD0001)

Each session carries a concept as its title; what happens in the project follows after the colon. Since 12 October the topics have moved back by one session, and Abstraction and Layers no longer has an input of its own. The schedule in ILIAS is the binding version.

1. 28.09. Kick-off: overview and setup
2. 05.10. Setup and first programs: devices handed out, Challenge 0
3. 12.10. Cutting Problems, Solving Problems with Computers: Challenge 0
   (19.10. cancelled, 26.10. excursion week, no sessions)
4. 02.11. Algorithms and Programs, Analog and Digital, Symbols and Information: Challenge 1 starts
5. **Wednesday 04.11., 09:45 to 13:00, online in Teams.** Measuring and Experimenting
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
