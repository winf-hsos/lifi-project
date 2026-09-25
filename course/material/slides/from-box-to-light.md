<!-- Lecture notes for the slides on `from-box-to-light`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/from-box-to-light.html -->

# Lecture notes: from box to light (Setup and first steps)

These notes explain the deck for the second half of the first session, for reading afterwards. It takes you from the unopened kit to a green LED: what is in the box, which tools you need and how they fit together, how to set them up, and how the workshop runs when one person looks after 24 teams. They follow the order of the slides (the numbers are frames, and build-up steps count separately) and can be read as a text of their own. The step-by-step instructions are on the website under "Required Software".

## Opening (Frame 3)

**What's in the box?** Every team gets two kits, and within an hour and a half, light should come out of one of them because you told it to. The way there leads through a handful of tools that form a chain. This deck shows the chain, and then you set it up.

## Part 1: your kit (Frames 4 to 9)

**Your device (Frames 5 to 8).** This is the real device, seen from the front. On the left sits the eye, a colour sensor that reports four numbers. On the right sits the lamp, an RGB LED, three little lamps in one. Between them stands a wall, so that the device does not see its own lamp. And inside there is a third board, the Master Brick, which connects both of them to your laptop through the USB socket at the back. That is all it takes, and nothing more will be added. The names of all the parts are on the hardware page of the website.

**It's yours until January (Frame 9).** Every team gets two kits, one for each of you, so you own both ends of the link and can try everything yourselves. You sign for your kit when you pick it up. Bring it every Monday and keep it in one piece: do not pull on the boards, and handle the USB cable with care, it is the most fragile part. If something breaks, say so right away; there are spare parts.

## Part 2: your tools (Frames 10 to 18)

**From your idea to the light (Frames 11 to 16).** Six links in a chain, from top to bottom. You decide what should happen. You tell your assistant in OpenCode, and it writes and explains a Python program, which you are meant to read and understand; it lives in your folder `my-code`. The program uses a small module, `lifi_hardware`, that speaks the language of the device. Below it runs a service, the Brick Daemon, which keeps the USB connection open. And at the bottom sits the device, lamp and eye, on your table. Each link only knows its neighbours. That will become important during the semester, under the name of layers. Today you install all of them.

**Your assistant (Frame 17).** OpenCode comes with a model that is already set up for this course. Your assistant knows the course, because it reads in your course folder: the pages of the website, the notes for every slide deck, the source code of the module. Ask it anything, as often as you like; it explains, installs and writes code. In the workshop it is the first place to ask, before the lecturer. What it cannot do is see your device. The lamp has the last word.

**Your key (Frame 18).** You get your key by email, and it is for you alone. It carries a budget, so use it for this course. You type it into OpenCode, in the provider settings, and nowhere else: not into a chat, not into a file, not into a screenshot. Whoever has your key works at your expense. When the budget runs out, that is not the end: OpenCode comes with free models, and they are good enough for a lot.

## Part 3: getting ready (Frames 19 to 31)

**Part 1, by hand (Frames 20 to 23).** Four steps you take yourselves, because before them there is no assistant yet that could help: install OpenCode Desktop; download the course folder as a ZIP from GitHub and unpack it, preferably somewhere like Documents and not in a cloud folder; open the folder in OpenCode; enter your key. The website shows every step for Windows and for macOS at docs.lifi-project.de/software.

**Part 2, your assistant takes over (Frames 24 to 28).** In the course folder you type `/onboarding`. From here on the assistant does the work, and you read along and confirm. It asks you three questions, then it installs what is missing: Python, the module `lifi_hardware`, VS Code, the Brick Daemon and the Brick Viewer. It checks every step before it takes the next one. When it asks, you plug in your device. When it asks whether it may run something: read first, then allow. And if you do not understand something, ask; that is what it is there for.

**The finish line (Frames 29 and 30).** At the end of `/onboarding` your LED lights up green, because your program told it to, and the sensor delivers three readings. At the same moment your device announces itself to the course server, and it appears in the team cockpit. From then on the cockpit shows what your lamp sends and what your sensor measures.

**Where are you? (Frame 31).** A checklist of six lines that stays on the wall during the workshop: OpenCode installed, course folder open, key entered, `/onboarding` started, LED green, device in the cockpit. If you are asked where you are, answer with the line. Whoever has the last line is done and helps the table next door.

## Part 4: how the workshop works (Frames 32 to 37)

**Stuck? Ask in this order (Frames 33 to 35).** First your assistant, with the complete error message. Then the team next to you, which may just have solved the same thing. Only then Nicolas. There is one lecturer and there are 24 teams; if everybody waits for him, nobody moves on. This is not a way of keeping you at a distance, it is how people work together in any job.

**How to ask your assistant (Frame 36).** Say what you wanted to happen. Paste what happened instead, the whole error and not just its last line. And ask why, not only how. A red error message is information, not a verdict. In the exam nobody asks whether the assistant knew.

**Every week (Frame 37).** Every week new material arrives, for example the template for the next challenge and the current state of the semester, which your assistant then knows too. The command `/update-semester` fetches it. Everything you write yourselves belongs in the folder `my-code`; the rest of the course folder is replaced when you update, without asking.

## Closing (Frame 38)

Until next Monday: whoever did not finish today completes the setup at home with `/onboarding`; the assistant helps there just as well. And read the pages "The Project" and "Challenge 0" on the website. Next week you write your first program of your own, and for that the light has to be on.
