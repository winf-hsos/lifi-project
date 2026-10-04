<!-- Lecture notes for the slides on `first-light`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/first-light.html -->

# Lecture notes: first light (Setup and first steps)

These notes explain the deck for the second half of the first session, for reading afterwards. It introduces your device, which you get in the second session, explains what your AI assistant is and how to work with it safely, walks you through the setup, and then builds your first program together with you: a countdown timer with a coloured lamp in the terminal. At the end it explains how our workshops run when one person looks after 24 teams. The notes follow the order of the slides (the numbers are frames, and build-up steps count separately) and can be read as a text of their own. The step-by-step installation instructions are on the website under "Required Software".

## Part 1: your device (Frames 3 to 14)

**Your device (Frame 3).** The title of this deck is a word from astronomy: first light is the first image a new telescope takes. Today your first light shines in the terminal: your first program shows a coloured lamp there. Next week the same lamp lights up on your device. Today you only see the device, in the picture and under the visualizer at the front; you get your own next Monday. Until then, your laptop gets ready for it, and you write your first program.

**What is on it (Frames 4 to 7).** This is the real device, seen from the front; with every step a yellow frame marks the part in question. On the left sits the eye, a colour sensor that reports four numbers. On the right sits the lamp, an RGB LED, three little lamps in one. Between them stands a wall, so that the device does not see its own lamp. And inside there is a third board, the Master Brick, which connects both of them to your laptop through the USB socket at the back. That is all it takes, and nothing more will be added. The names of all the parts are on the hardware page of the website.

**Yours from next Monday (Frame 8).** Every team gets two devices, one for each of you, so you own both ends of the link and can try everything yourselves. You get them next Monday, sign for them, and keep them until the final in January. Find your partner by then: next Monday every team of two gets its devices. Today you prepare your laptop, so you can start right away when the device arrives.

**From your idea to the light (Frames 9 to 14).** Six links in a chain, from top to bottom. You decide what should happen, and you write code. Your assistant in OpenCode helps you write the program and understand it; the program is the code you write together, and it lives in your folder `my-code`. You are meant to read and understand every line of it. The program uses a small module, `lifi_hardware`, that speaks the language of the device. Below it runs a service, the Brick Daemon, which keeps the USB connection open. And at the bottom sits the device, lamp and eye, on your table. Each link only knows its neighbours. That will become important during the semester, under the name of layers. Today you install everything except the last link.

## Part 2: your assistant (Frames 15 to 50)

**Do you know who these are? (Frames 16 and 17).** Three logos, which you may or may not have seen before. On the left is Claude Code from Anthropic, in the middle Codex from OpenAI, the company behind ChatGPT, and on the right OpenCode, free and open source, which is the one we use. All three are AI agents for programming, and many developers work with one of them every day. But what makes such an agent different from ChatGPT, which most of you know?

**You know this already (Frames 18 to 23).** Most of you have worked with ChatGPT, Gemini or Copilot: you ask a question, it answers, and then it is your turn again. An agent gets a task instead, and works on it until it is done. A chat gets what you paste into it; an agent reads the files in your folder itself. From a chat you copy the code into a file; an agent writes the file itself. After a chat you run the program yourself and report back; an agent runs it and reads the result, error messages included. In a chat you decide what comes next; an agent tries again until it works. Tools as such are not the difference: chats can search the web or run code in their own environment, too. The difference is the loop. An agent solves a task on its own, in many steps, right where the work is: in your folder, with your tools, without you copying things back and forth between windows.

**The agent loop (Frames 24 to 29).** This is what the loop looks like. You give a task, for example: my timer crashes when I type five, find out why. The agent thinks about what to do next. It acts with a tool: it reads a file, changes a file, or runs the program; before changes and commands it asks you. It checks the result, for example the output in the terminal. If the task is not done yet, it starts again, as often as needed; when it is done, it comes back to you. You stand at both ends: you phrase the task, and you check whether the result is right.

**OpenCode (Frame 30).** Your assistant is OpenCode, set up for this course. It works on your laptop, in your course folder, with your files. It uses tools: it reads and writes files and runs programs and commands. It knows the course, because it reads in your course folder: the pages of the website, the lecture notes for every slide deck, the source code of the module `lifi_hardware`. In the workshop it is the first place to ask. What it cannot do is see your device. From next week on, the lamp has the last word, and you have to measure.

**The program and the model (Frames 31 to 37).** Two things are easily mixed up, and the drawing separates them. In the middle sits OpenCode, the program on your laptop: it shows you the chat, and below it are your files and the terminal, which it can reach. The thinking is done by a language model, and that model does not run on your laptop but on a server somewhere else; that is why it sits at the top, in the cloud. OpenCode sends it your task, what it has read from your files, and the results of the last steps. The model answers with the next step: read this file, change that one, run this program. So the model decides what should happen on your computer, and OpenCode carries it out, on your laptop, after asking you. This is the loop from before, spread across two computers. There are many models: free and paid ones, fast ones, and some that are especially good at code. In OpenCode you choose one below the input field. And from this follows the most important point: everything you type, and everything the assistant reads from your files, travels to that server.

**Your model (Frame 38).** You start with the free models that come with OpenCode. They work right away, without a key, and your course folder has already selected one of them. Free models come and go: if the preset one stops answering, pick another free one in the model selection below the input field. If a stronger model is needed later, you may get a key for it; you will hear when. And one rule holds for every key, marked in red: a key goes into OpenCode's provider settings and nowhere else. Never into a chat, a file or a screenshot. Whoever has a key works at its owner's expense.

**Its memory: the context window (Frames 39 to 43).** The model itself remembers nothing. What it knows is in its context window: your messages, its answers, the files it has read, the output of commands, and the instructions for this course. That is everything that happened in this session, and nothing else; a new session starts from zero. New things always enter from the right, as the arrow in the drawing shows, and the newest one sits at the entrance. The window has a fixed size, counted in tokens, which are roughly pieces of words; a token is about three quarters of an English word. When the window is full, OpenCode compacts it: the older parts shrink to a summary, as the grey boxes on the left show. OpenCode calls this compact, and you will see the word when it happens; you can also start it yourself with the command `/compact`. Details get lost on the way, and the assistant suddenly seems forgetful. Hence the rule of thumb: a new task gets a new session, with one sentence about what it is about. And a memory that lasts beyond a session? OpenCode does not have one built in, unlike ChatGPT. What should last goes into a file that it reads at every start; for you, those are the instructions for this course, elsewhere usually a file called `AGENTS.md`. You can reopen old sessions in OpenCode and continue them, but that is an archive, not a memory.

**Careful, not scared (Frames 44 to 50).** A program that changes files and runs commands on your computer deserves attention, not fear. The course folder is set up so that nothing happens without you. First, it asks: before it changes a file or runs a command, it waits for your OK. Read what it wants to do, then allow it; whoever clicks "allow" without reading hands over control. Second, it works in your course folder, so keep private files out of it. Third, it can be wrong, and it sounds just as sure when it is. Run it, measure it, check it; that is the principle of the whole course. Fourth, it can make mistakes when it acts, for example overwrite or delete a file it should have left alone. Usually that happens after an OK given too quickly. Keep a backup of everything that matters to you, for example a copy of your folder `my-code` somewhere else from time to time. OpenCode can take back the assistant's last changes with `/undo`, but do not rely on that alone. Fifth, you can stop it at any time with the stop button, when it heads in the wrong direction. Sixth, in red: what you write in the chat goes to the model's server. No passwords, no keys, no personal data, neither yours nor anybody else's. You decide what it may do, and that is the point.

## Part 3: getting ready (Frames 51 to 61)

**Part 1, by hand (Frames 52 to 54).** Three steps you take yourselves, because before them there is no assistant yet that could help: install OpenCode Desktop; download the course folder as a ZIP from GitHub and unpack it, preferably somewhere like Documents and not in a cloud folder; open the folder in OpenCode and start a session. You need no key for this: the course folder starts with a free model. The website shows every step for Windows and for macOS at docs.lifi-project.de/software.

**Part 2, your assistant takes over (Frames 55 to 59).** In the course folder you type `/onboarding`; the picture shows what happens next, package by package. From here on the assistant does the work, and you read along and confirm. It asks you three questions, then it installs what is missing: Python, the module `lifi_hardware`, VS Code, the Brick Daemon and the Brick Viewer. It checks every step before it takes the next one. When it asks whether it may run something: read first, then allow. As long as you have no device, it skips the device test at the end; that test follows next week.

**The finish line (Frames 60 and 61).** At the end of `/onboarding` everything your device needs is installed, and your laptop is ready. The lines about the device in the final check still report an error, which is right for today. Next Monday you plug in your device, and your LED lights up green, like the one in the picture, because your program told it to.

## Part 4: your first program (Frames 62 to 116)

Every code block on these slides has a copy button at its top right. Before each of the five steps, a slide shows where we are: the steps done so far are ticked, the next one is highlighted. The slides are on the website under "Required Software".

**A program is a file (Frames 63 to 65).** Open your course folder in VS Code with *File > Open Folder*. On the left you see the folder `my-code`. Right-click it, choose *New File* and call the file `hello.py`. The ending `.py` tells your computer and VS Code that this file contains Python; VS Code then offers to install its Python extension, which you accept. A program is plain text in a file at first. You could write it in any text editor. It only becomes a program when Python reads the text and carries it out, line by line.

**Your first line (Frames 66 to 68).** Type `print("Hello, world!")` into the file. `print` means: show this. What stands between the quotation marks is text, and it appears exactly as written. Save with Ctrl+S (Cmd+S on a Mac). Then open a terminal in VS Code via *Terminal > New Terminal*. The terminal is the command line: you type a command, and the computer answers. It starts in your course folder. `cd my-code` changes into your folder, and `python hello.py` tells Python to read this file and run it; on a Mac the command is `python3`. The answer appears below: `Hello, world!` That is your first program. VS Code also has a play button at the top right that does the same thing, but it is worth seeing once what happens behind it.

**Asking and answering (Frames 69 to 72).** Two lines, and the program talks to you:

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

Run it again; the up arrow in the terminal brings back the last command. The program asks, waits, and greets you by name. `input()` shows the question, waits until you press Enter, and hands back what you typed. The equals sign does not mean "is equal to" here, but "remember this under this name": `name` is a variable, a name for a value, so you can use it again. And `+` joins pieces of text.

**The task (Frame 73).** Write a timer for the terminal. It asks how many seconds, then counts down, one line per second. A coloured lamp shows how it stands: green while it runs, yellow in the last five seconds, red when time is up. Today the lamp is a coloured block in the terminal. Next week it is the LED on your device, and the timer hardly changes.

**Cut it into steps (Frames 74 to 80).** Whoever tries to write the whole program at once gets lost. So we cut it into steps: what has to happen, in which order? First get the number of seconds from the user. Then check if the input is valid. Then count down each second. Then show a coloured lamp. And finally decide which colour. Each step has its Python tool: `input()`, `while`, `for`, `def`, `if` and `else`. You meet all five for the first time today, and all five come back during the semester. Run the program after each step; then, when something breaks, you know the fault is in the last step. This way of cutting a problem is the topic of the next session, Cutting Problems; the slide links its concept page, https://docs.lifi-project.de/concepts/problem-decomposition.html.

**And your assistant? (Frames 81 to 85).** Your assistant could write the timer in ten seconds. Then you would have a program and would have learned nothing, and in the exam it does not sit next to you. Use it as a teacher. Ask it to explain what a line does, for example what `input()` hands back. Let it read your file ("read my `timer.py`, is step 2 right?"); it can, because it works in your folder, and you do not have to paste anything. Let it run the program itself, even with a wrong input ("run it with five as input, what goes wrong?"), and read the error; that is the loop from before. And ask for a hint instead of the solution. It is set up for this course to go through the steps with you.

**Step 1: get the number of seconds (Frames 86 to 89).** Create a new file `timer.py` in `my-code`:

```python
text = input("How many seconds? ")
seconds = int(text)
print("Timer:", seconds, "seconds")
```

`input()` always hands back text, even if you type 20: for Python that is the characters two and zero, not a number. Try `print(text + 1)`, and Python complains that it cannot add text and a number. `int()` turns the text into a whole number, so you can count with it. The third line only tests whether that worked.

**What if someone types five? (Frames 90 to 93).** Start the timer and type `five` instead of a number. The program stops with an error message:

```
Traceback (most recent call last):
  File "…\my-code\timer.py", line 2, in <module>
    seconds = int(text)
ValueError: invalid literal for int() with base 10: 'five'
```

It looks alarming, but it is information, not a verdict. Read it from the bottom. The last line says what went wrong: a `ValueError`, because `int()` cannot make a number out of "five". The lines above say where: in which file, in line 2, and the line itself. You can usually skip the rest at the top. On the slide, what you typed is white and what Python answers is grey. If you are stuck, ask your assistant. You do not even have to paste the message: it can start the program itself, with five as input, and read the error. Then let it explain what the message means.

**Step 2: check if the input is valid (Frames 94 to 97).** Two new lines go between `input` and `int`:

```python
text = input("How many seconds? ")
while not text.isdigit():
    text = input("Digits only, please: ")
seconds = int(text)
```

`text.isdigit()` asks the text: do you consist of digits only? The answer is true or false; true for "20", false for "five", and also false for "-3" and "2.5". `while` means: as long as. As long as the text is not a number, the program asks again. The indented line belongs to the loop. In Python, indentation is not decoration: it decides what is repeated. Try "five", then 20. And ask your assistant what happens when somebody types 0.

**Step 3: count down each second (Frames 98 to 101).**

```python
import time

for remaining in range(seconds, 0, -1):
    print(remaining, "s")
    time.sleep(1)

print("time is up!")
```

`import time` brings in a tool from Python that deals with time; this line belongs at the very top of the file. `range(seconds, 0, -1)` produces the numbers from `seconds` backwards down to 1: the 0 is the limit and is itself not included, which is how Python does it everywhere. `for` means: for each of these numbers, and `remaining` is the name under which the current number stands. The two indented lines run once for every number: show it, wait one second. The last line is not indented, so it runs once, after the loop. Try moving `time.sleep(1)` out of the indentation and watch what happens.

**Step 4: show a coloured lamp (Frames 102 to 106).** We need the lamp three times, in three colours. Instead of writing the same lines three times, we give them a name. That is a function:

```python
def lamp(r, g, b):
    on = f"\033[48;2;{r};{g};{b}m"
    off = "\033[0m"
    print(on + " " * 12 + off, end=" ")

lamp(0, 200, 0)
print("running")
```

The strange characters with the backslash are instructions to the terminal: switch this background colour on, and afterwards off again. In between are twelve spaces, which become coloured that way. `def` means define. `r`, `g` and `b` are parameters, placeholders for values; you fill in the values when you call the function: red, green and blue, each from 0 to 255. `lamp(0, 200, 0)` is green. The function belongs near the top of the file, below `import time`; the last two lines are only for trying it out. If you see strange characters instead of a colour, your program runs in the old Windows console; ask your assistant. And here is the relief: you do not have to understand the codes inside the function. You may, but you do not have to.

**Why functions help (Frames 107 to 111).** This is one of the most important ideas in programming, and you have just used it: a function hides the details behind a name. To use `lamp()`, you need to know what it does, show a lamp in the colour r, g, b, but not how it does it. You have experienced this twice today without noticing. `print()` and `input()` are functions too, and there is far more inside them than inside `lamp()`: encoding characters, talking to the terminal, waiting for the keyboard. Did you miss their insides? Next week you swap `lamp()` for `led.set_color(r, g, b)`, and behind it hides a whole device, with USB, the Brick Daemon and circuit boards. You still use it with one line. That is how complexity is handled: not by understanding everything at once, but by packing it into parts whose insides you do not have to know every time. It comes back during the semester, under abstraction and layers. And if you are curious anyway, open it up with your assistant: it explains every character of `lamp()`.

**Step 5: decide which colour (Frames 112 to 114).** The last ingredient is a decision. The new lines are the yellow ones:

```python
for remaining in range(seconds, 0, -1):
    if remaining <= 5:
        lamp(255, 200, 0)   # yellow
    else:
        lamp(0, 200, 0)     # green
    print(remaining, "s")
    time.sleep(1)

lamp(255, 0, 0)             # red
print("time is up!")
```

In every round of the loop the program asks: are there five seconds or fewer left? Then yellow, otherwise green. After the loop, red once. `if` checks a condition that is true or false. If it is true, the indented block below it runs; otherwise the block below `else` runs. Exactly one of the two, never both. What follows the hash sign is a comment: it is for people, and Python skips it. Try it with 8 seconds.

**The whole program (Frames 115 and 116).** All five steps are ticked. The program has 23 lines; the slide shows only the beginning, but its copy button copies all of them. Paste them into `timer.py` and read them in VS Code, from top to bottom. Python reads the same way. That is why `import time` stands at the very top, then the function, and only after that the part that uses it: a function has to be defined before it is called. Make sure you understand every line, and ask your assistant about each one you cannot explain.

## Part 5: how our workshops work (Frames 117 to 124)

**Stuck? Ask in this order (Frames 118 to 121).** First your assistant; let it run the program and read the error. Then your partner. Then the team next to you, which may just have solved the same thing. Only then Nicolas. There is one lecturer and there are 24 teams; if everybody waits for him, nobody moves on. This is not a way of keeping you at a distance, it is how people work together in any job.

**How to ask your assistant (Frame 122).** Say what you wanted to happen. Let it run the program itself, so it sees the whole error; where it cannot, because something only happens on your screen, send it a screenshot, since your assistant can read pictures. And ask why, not only how. An error message is information, not a verdict. In the exam nobody asks whether the assistant knew.

**Every week (Frame 123).** Every week new material arrives, for example the template for the next challenge and the current state of the semester, which your assistant then knows too. The command `/update-semester` fetches it. Everything you write yourselves belongs in the folder `my-code`; the rest of the course folder is replaced when you update, without asking.

**Where are you? (Frame 124).** A checklist of six lines that stays on the wall during the workshop: OpenCode installed and course folder open, assistant answers, `/onboarding` done, `hello.py` runs, timer counts down, timer shows its colours. If you are asked where you are, answer with the line. Whoever has the last line is done and helps the table next door, or extends the timer, for example with a display in minutes and seconds.

## Closing (Frame 125)

Until next Monday: form a team of two; if you have nobody yet, tell Nicolas, and we will find someone. Finish the setup and your timer; your assistant helps at home just as well, and the slides with the code are on the website. Read the pages "The Project" and "Challenge 0". Next week you get your devices, and the lamp in the terminal becomes the LED: you swap `lamp()` for `led.set_color()`, and your timer lights up on the table.
