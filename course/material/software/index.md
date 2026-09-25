# Required Software

Online: <https://docs.lifi-project.de/software/index.html>

Six programs have to be on your laptop before your first line of code. All of them are free, and all of them run on Windows and on macOS.

| Program | What you need it for | Where to get it |
|---|---|---|
| **Visual Studio Code** | the editor you write in | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git** | fetches the course folder and the `lifi_hardware` module | [git-scm.com](https://git-scm.com/downloads) |
| **OpenCode** | your AI assistant | [opencode.ai](https://opencode.ai/) |
| **Python** | the language you program in | [python.org](https://www.python.org/downloads/) |
| **Brick Daemon** | connects your hardware to the laptop | [Tinkerforge downloads](https://www.tinkerforge.com/en/doc/Downloads.html) |
| **Brick Viewer** | shows whether the hardware is recognised, and helps you find faults | [Tinkerforge downloads](https://www.tinkerforge.com/en/doc/Downloads.html) |

On top of these comes the module `lifi_hardware`, which is how your programs talk to your device. It is installed with a single command and brings the Tinkerforge library with it.

## What each program does

**Python** is the language you write your sender and receiver in. It reads almost like English, which makes it a good first language, but it is not a toy. Python is one of the most widely used languages there are: data analysis, artificial intelligence, automation, scientific computing and a large part of the web run on it. What you learn here you can use straight away elsewhere.

**Git** you need in this project only for fetching files: once for the course material, which holds everything your AI assistant needs to know about the module, and once for installing `lifi_hardware`, which is also fetched through Git. When something is added during the course, you get the new version with one command. Git can do a great deal more, but you will not need it here.

**Visual Studio Code** is the editor. This is where you write your code, where you see your files, and where the terminal lives in which you start your programs.

**OpenCode** is the AI assistant. It runs in the terminal, which means it also runs in the terminal inside VS Code, and it can read and change your project files. How to work with it is on [its own page](../ai/index.md).

**Brick Daemon** is a background program. It runs invisibly and translates between the hardware on the USB port and your Python programs. Without it your program cannot find the device. When one day nothing works at all, "is the Brick Daemon even running?" is one of the first questions to ask.

**Brick Viewer** is a window onto your hardware. It shows you which parts are recognised, lets you switch the LED by hand and watch the sensor values run, all without a line of your own code. For finding faults it is worth gold: if it works in the Brick Viewer, the fault is in your program. If it does not, the fault is somewhere before your program.

## Installation step by step

The installation has two parts. In the first part you install three programs by hand and fetch the course folder. That is the minimum your assistant needs to run. In the second part your assistant takes over: it walks you through the rest one step at a time and checks each step itself, on your laptop.

Installations rarely go through at the first attempt, and that is not your fault. If you get stuck in the first part, keep the error message word for word. Somebody who can help will want to see exactly that.

## Part 1: until your assistant runs

### 1. Visual Studio Code

Download the editor from [code.visualstudio.com](https://code.visualstudio.com/) and install it. Later, when you open your first Python file, it offers to install the Python extension. Accept.

Two things to try right away:

- **Open a folder** via *File > Open Folder*. VS Code always works with a folder, not with single files.
- **Open a terminal** via *Terminal > New Terminal*. This window at the bottom of the editor is the command line where you start your programs, and where you continue in a moment. From now on, every command on this page goes into this terminal.

### 2. Git

#### Windows

Download Git from [git-scm.com/downloads](https://git-scm.com/downloads) and install it. You can accept the installer's defaults throughout.

This also installs **Git Bash**, a terminal you need for OpenCode in the next step.

To check, close VS Code completely and open it again (a program you just installed only becomes visible to VS Code after a restart), then open a terminal and type:

```powershell
git --version
```

#### macOS

In the Terminal, simply type

```bash
git --version
```

If Git is missing, macOS offers to install the Command Line Tools by itself. Accept and wait until it is done. Alternatively via [Homebrew](https://brew.sh): `brew install git`.

### 3. OpenCode

OpenCode runs in the terminal. Use the terminal inside VS Code for it.

#### Windows

First make **Git Bash** the standard terminal of VS Code, once: press Ctrl+Shift+P, type `Terminal: Select Default Profile`, press Enter and choose **Git Bash**. OpenCode only works in this terminal, and this way every new terminal is a Git Bash. Then open a new terminal (*Terminal > New Terminal*) and type:

```bash
curl -fsSL https://opencode.ai/install | bash
```

#### macOS

In the terminal in VS Code:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Alternatively via [Homebrew](https://brew.sh): `brew install sst/tap/opencode`.

To check, open a new terminal and type `opencode --version`. A version number should appear.

Do not start it yet. OpenCode needs a language model to talk to, and the course folder in the next step sets that up for you.

### 4. The course folder and your assistant

The course folder holds everything your assistant needs to know about this module, and it is the folder you work in for the rest of the semester.

In the terminal in VS Code, type

```bash
git clone https://github.com/winf-hsos/lifi-project.git
```

Git creates a folder `lifi-project` in the folder the terminal was in, usually your user folder. Open exactly that folder via *File > Open Folder*. From now on, always open this folder when you work on the project. Inside it you will see:

- `my-code`: **your folder.** Everything you write goes here, and your copy of each challenge lands here.
- `course`: the course material. Your assistant reads it; you do not change it.
- a few more files for OpenCode, which you can ignore.

Now give your assistant its key. At the start of the course you get a personal key for the language model, a long line of characters beginning with `sk-`. In VS Code choose *File > New File*, name the file exactly `openai.key`, paste the key into it, and save. The file belongs directly into `lifi-project`, next to `README.md`. Nothing else goes into it.

The key is yours and it costs money every time the assistant answers, so treat it like a password: do not send it to anyone, do not paste it into a chat, not even the one with your assistant. The file stays on your laptop. Git has been told to ignore it, so it cannot end up anywhere by accident.

If you are working through this course on your own, without a key from us, put a key of your own from [platform.openai.com](https://platform.openai.com/api-keys) into the file. It works the same way.

Then open a new terminal in VS Code and type

```bash
opencode
```

The assistant starts with the course model already selected. If it reports that `openai.key` does not exist, the file has a different name or sits in a different folder. If it reports that the key is incorrect, open the file and check that it contains the key and nothing else.

## Part 2: your assistant takes over

In OpenCode, type

```
/onboarding
```

In the first session everyone does this together. Your assistant asks you three short questions, then installs the rest with you and checks every step: Python, the Brick Daemon and Brick Viewer, and the module `lifi_hardware`. At the end it tests your device: your LED lights up green, and the sensor reports its first readings.

You do not need the instructions below for that. They are here so you can look something up, and for everyone working on their own.

When something is added to the course during the semester, type `/update-semester` in OpenCode. The assistant fetches the new version for you. You do not need to know Git for it, and your folder `my-code` is never touched.

### Python

#### Windows

Download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it.

**Important:** in the first window, tick **"Add python.exe to PATH"** before you click "Install Now". Without that tick the command line will not find Python later, and this is by far the most common stumbling block.

To check, open the **Command Prompt** and type

```powershell
python --version
```

A version number should appear, something like `Python 3.13.1`.

#### macOS

A Mac comes with an older Python preinstalled, but you should not use that one. Download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it.

To check, open the **Terminal** and type

```bash
python3 --version
```

A version number should appear, something like `Python 3.13.1`.

Remember: on a Mac the command is `python3`, not `python`.

### Brick Daemon and Brick Viewer

You get both from the [Tinkerforge download page](https://www.tinkerforge.com/en/doc/Downloads.html). Download the version for your operating system and install it.

On **Windows** these are two `.exe` installers, on **macOS** two `.dmg` packages that you open and drag into the Applications folder.

The Brick Daemon starts by itself afterwards and keeps running as a background service. You do not see it, and that is normal.

### The module `lifi_hardware`

This is how your Python programs talk to the hardware. `/onboarding` installs it for you, and `/update-semester` updates it when a new version appears. By hand, in the terminal:

```bash
pip install git+https://github.com/winf-hsos/lifi-hardware.git
```

On a Mac, `pip3` instead of `pip` if needed.

The package brings the Tinkerforge library along as a dependency, so you do not install that separately. And because the address starts with `git+`, `pip` fetches the package through Git. That is why Git from step 2 had to come first.

### Check that everything works together

Connect a device over USB and start the Brick Viewer. If your Master Brick shows up there with the LED and the colour sensor, the installation is complete. Click around and switch the LED on by hand. That is not programming yet, but it is proof that everything is talking to everything else.

### When something does not work

The questions that help most often:

1. Is the Brick Daemon running? Without it no program finds the hardware.
2. Does the Brick Viewer show your device? If not, the fault is before your code. Unplug the USB cable and plug it in again: that cures a surprising number of cases.
3. Are you using `python` or `python3`, `pip` or `pip3`? On a Mac it is almost always the one with the 3.

Or ask your assistant to check your setup. It runs the same test as in `/onboarding` and tells you what is missing.
