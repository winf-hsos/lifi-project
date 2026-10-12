# Challenge 0: The Spark

Can you bring your device to life?

## What you do

Six tasks, one Python file each. Wherever it says `TODO`, your code is missing. Work through them in order, each one builds on the one before.

| | File | What you learn |
|---|---|---|
| 1 | `task_1_light_on.py` | calling a function and handing it values |
| 2 | `task_2_blink.py` | a loop, which means doing something several times |
| 3 | `task_3_color_cycle.py` | a list and how to go through it |
| 4 | `task_4_measure.py` | a function that gives values back, and measuring one situation at a time |
| 5 | `task_5_react.py` | a condition, which means doing something different depending on the situation |
| 6 | `task_6_human_receiver.py` | what a receiver actually has to manage |

There are no more building blocks than these. Everything you program for the rest of the semester is made of exactly three things: one after the other, repeated, and under a condition.

## Trying it out

Run one task at a time, here task 3:

```bash
python task_3_color_cycle.py
```

On a Mac use `python3` instead of `python` if needed. Task 5 keeps running until you stop it with Ctrl+C.

## Task 5 is the most interesting

This is where your program makes a decision for the first time: it measures, compares and does something different depending on the result. In small, that is already what the whole semester is about.

You have to find the threshold yourself. In task 4 you take one reading per Enter: room light, the sensor covered with your hand, your phone torch from far away and close up. The clear value `c` is the brightness, and your threshold goes between "covered" and "torch". If `c` sticks at 65535, the sensor is overloaded; hold the torch further away.

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
