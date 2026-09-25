# Challenge 0: The Spark

Can you bring your device to life?

## What you do

`tasks.py` holds six tasks. Wherever it says `TODO`, your code is missing. Work through them in order, each one builds on the one before.

| | Task | What you learn |
|---|---|---|
| 1 | Light on | calling a function and handing it values |
| 2 | Blink | a loop, which means doing something several times |
| 3 | Colour cycle | a list and how to go through it |
| 4 | Measure | a function that gives values back |
| 5 | React | a condition, which means doing something different depending on the situation |
| 6 | The human as receiver | what a receiver actually has to manage |

There are no more building blocks than these. Everything you program for the rest of the semester is made of exactly three things: one after the other, repeated, and under a condition.

## Trying it out

One single task, here task 3:

```bash
python tasks.py 3
```

All of them one after the other:

```bash
python tasks.py
```

On a Mac use `python3` instead of `python` if needed.

Task 5 keeps running until you stop it with Ctrl+C. When you run all tasks in one go, task 6 only starts after that.

## Task 5 is the most interesting

This is where your program makes a decision for the first time: it measures, compares and does something different depending on the result. In small, that is already what the whole semester is about.

You have to find the threshold yourself. Run task 4, hold your hand between the devices and watch how the value `C` changes. That number is the brightness.

## Task 6 teaches you the most

Here you are the receiver yourself. The program sends a sequence of colours, one of you writes it down without looking at the screen, and afterwards you compare.

The first time this works without effort. It gets interesting when you change exactly one thing each time: send faster, use more colours, do not announce when it starts, send the same colour twice in a row.

Write down what made it fail each time. That list is pretty much the list of problems your program will have to solve in the coming weeks. You will have found it yourselves instead of having it explained to you.

## At the acceptance test

You show the tasks running, on both devices of your team.

Then you are given a small change to make on the spot. For example: "Make it blink twice as fast" or "Turn the condition in task 5 around."

This is not a trap, it is the start of a habit: you should be able to change your own code, even when parts of it were written with the help of your assistant.

## When nothing works

1. Is the Brick Daemon running? Without it your program cannot find the hardware.
2. Does the Brick Viewer show your device? If not, the fault is before your code.
3. Is the command `python` or `python3` on your laptop?

Or ask your assistant: type `/onboarding` in OpenCode, and it checks your setup step by step.
