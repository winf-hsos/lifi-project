# LiFi Project: course repository

This is your working folder for the LiFi Project in the module Digitization and Programming at Hochschule Osnabrück. Everything else about the project is on the website: <https://docs.lifi-project.de/>

## What is in here

| | |
|---|---|
| `AGENTS.md` | the instructions your AI assistant follows. You do not need to read it, but you may. |
| `NOW.md` | where the semester stands. Your assistant reads it at the start. |
| `course/` | the course material as plain text, so your assistant can look things up. The same content as the website. |
| `my-code/` | **your own folder.** Your copy of each challenge template lands here (`my-code/challenge-0/` and later ones), and everything you write belongs here. Updates never touch it. |
| `templates/` | the original templates, one per challenge, released during the semester |
| `tools/` | two small scripts your assistant uses to check your laptop and to update this folder |

## Getting started

1. Open this folder in Visual Studio Code: *File > Open Folder*.
2. Create your key file: *File > New File*, name it exactly `openai.key`, paste the personal key you got from your lecturer, save. Nothing else goes into this file. It stays on your laptop: Git ignores it, and you never share it.
3. Open a terminal: *Terminal > New Terminal*.
4. Type `opencode` and press Enter. Your assistant starts with the course model already selected and knows about this course.

5. Type `/onboarding` and press Enter. Your assistant asks you a few questions and checks that your laptop and your device are ready.

After that, ask it anything, for example: "Help me with task 1 of Challenge 0" or "Explain what a loop is, with an example".

## Getting updates

New templates and material are added during the semester. To get them, type `/update-semester` in OpenCode. You do not need to know Git: the assistant runs a script that fetches the new version, saves anything you might have changed in the course files, and never touches your folder `my-code/`.
