# Required Software

Online: <https://docs.lifi-project.de/software/index.html>

Six programs have to be on your laptop before your first line of code. All of them are free, and all of them run on Windows and on macOS.

| Program | What you need it for | Where to get it |
|---|---|---|
| **Python** | the language you program in | [python.org](https://www.python.org/downloads/) |
| **Git** | fetches the course material and the `lifi_hardware` module | [git-scm.com](https://git-scm.com/downloads) |
| **Visual Studio Code** | the editor you write in | [code.visualstudio.com](https://code.visualstudio.com/) |
| **OpenCode** | your AI assistant | [opencode.ai](https://opencode.ai/) |
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

Keep to the order, some steps build on earlier ones. Allow an afternoon. Installations rarely go through at the first attempt, and that is not your fault.

As soon as OpenCode from step 4 is running, you can ask it for help with everything that follows. Paste an error message, or take a screenshot of the window you are stuck at and hand it over: the assistant can read screenshots. It will walk you through the remaining steps, make sense of error messages and check whether something is missing. More on what it can do for you under [Working with your AI assistant](../ai/index.md).

If you still get stuck, keep the error message word for word. Somebody who can help will want to see exactly that.

### 1. Python

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

### 2. Git

#### Windows

Download Git from [git-scm.com/downloads](https://git-scm.com/downloads) and install it. You can accept the installer's defaults throughout.

This also installs **Git Bash**, a terminal you will need for OpenCode in step 4.

To check, in the Command Prompt:

```powershell
git --version
```

#### macOS

In the Terminal, simply type

```bash
git --version
```

If Git is missing, macOS offers to install the Command Line Tools by itself. Accept and wait until it is done. Alternatively via [Homebrew](https://brew.sh): `brew install git`.

### 3. Visual Studio Code

Download the editor from [code.visualstudio.com](https://code.visualstudio.com/) and install it. At the first start it offers to install the Python extension. Accept.

Two things to try right away:

- **Open a folder** via *File > Open Folder*. VS Code always works with a folder, not with single files.
- **Open a terminal** via *Terminal > New Terminal*. This window at the bottom of the editor is the command line where you start your programs, and where you continue in a moment.

### 4. OpenCode

OpenCode runs in the terminal. Use the terminal inside VS Code for it.

#### Windows

Open a terminal in VS Code and choose **Git Bash** at the top right of the terminal window. There:

```bash
curl -fsSL https://opencode.ai/install | bash
```

#### macOS

In the Terminal:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Alternatively via [Homebrew](https://brew.sh): `brew install sst/tap/opencode`.

To check: `opencode --version`.

After that, OpenCode has to be connected to a language model. Which model you use and how you get access depends on where you are taking this course; your course will tell you. If you are working on your own, the [OpenCode documentation](https://opencode.ai/docs/) lists the providers it works with.

### 5. Brick Daemon and Brick Viewer

You get both from the [Tinkerforge download page](https://www.tinkerforge.com/en/doc/Downloads.html). Download the version for your operating system and install it.

On **Windows** these are two `.exe` installers, on **macOS** two `.dmg` packages that you open and drag into the Applications folder.

The Brick Daemon starts by itself afterwards and keeps running as a background service. You do not see it, and that is normal.

### 6. The module `lifi_hardware`

This is how your Python programs talk to the hardware. In the terminal:

```bash
pip install git+https://github.com/winf-hsos/lifi-hardware.git
```

On a Mac, `pip3` instead of `pip` if needed.

The package brings the Tinkerforge library along as a dependency, so you do not install that separately. And because the address starts with `git+`, `pip` fetches the package through Git. That is why Git from step 2 had to come first.

When a new version of the module appears during the course, you get it with

```bash
pip install --upgrade --force-reinstall git+https://github.com/winf-hsos/lifi-hardware.git
```

### 7. Fetch the course material

This gives you the knowledge base of the module and the instructions your assistant follows.

```bash
git clone <ADDRESS-OF-THE-REPOSITORY>
```

Then open the resulting folder in VS Code. When something is added during the course, you get the new version with `git pull`.

### 8. Check that everything works together

Connect a device over USB and start the Brick Viewer. If your Master Brick shows up there with the LED and the colour sensor, the installation is complete. Click around and switch the LED on by hand. That is not programming yet, but it is proof that everything is talking to everything else.

### When something does not work

The three questions that help most often:

1. Is the Brick Daemon running? Without it no program finds the hardware.
2. Does the Brick Viewer show your device? If not, the fault is before your code.
3. Are you using `python` or `python3`, `pip` or `pip3`? On a Mac it is almost always the one with the 3.
