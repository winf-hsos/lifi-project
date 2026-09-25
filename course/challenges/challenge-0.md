# Challenge 0: The Spark

Online: <https://docs.lifi-project.de/challenges/challenge-0.html>

Before anything can travel through the air, your laptop and your box have to talk to each other at all. So this first challenge asks only one question, and it is a modest one on purpose:

> **Can you bring your device to life?**

Nothing is transmitted yet. This is about the tools: the editor, your first lines of Python, your first conversation with the AI assistant. If it takes you a while, you are not behind. Most people who did this before you had never seen a terminal either.

At the end there is a single sign of life. Your LED shines because you told it to, and the sensor across the table notices. That is all, and it is enough.

## The task

On **each** of your two devices, a program does two things:

1. The LED shines in a colour you set in the program.
2. The sensor prints its four readings to the console, again and again.

Each of you does this on your own laptop with your own box. When you are done, you should be able to switch the LED to another colour and watch the numbers of the sensor opposite change.

## What is new

Everything. For most of you this is the first program you have ever written.

Two tools are new as well, and they stay with you for the whole project: the terminal, where you start programs, and the AI assistant, which you work with.

## What is measured

Nothing. There is no competition in this challenge.

It is, however, the **prerequisite** for everything that follows. Without a running device you cannot even begin Challenge 1.

## Showing it works

Run your program and show it: the LED shines, readings appear. Then make one small change while someone watches, for example "now make the LED blue". This is not a test. It is the start of a habit that stays with you until the end: you should be able to change your own code, on the spot, and know what will happen.

## What you hand in

Only the running program. No documentation yet.

## Concepts you need

- [Problem decomposition](../concepts/problem-decomposition.md)

## Traps we know about

**The Brick Daemon is not running.** Without it your program cannot find the hardware, no matter how correct the code is. Check this first, every time.

**Python is not found.** On Windows this is almost always the missing tick at "Add python.exe to PATH" during installation. On a Mac the command is `python3`, not `python`.

**The Brick Viewer does not show the device.** Then the problem is before your code, not in it. Cable, port, power.

The full installation guide is under [Required Software](../software/index.md#installation).

## Be the receiver yourself, once

To finish, a task without a sensor. Your program sends a sequence of colours, and one of you writes them down without looking at the screen. Then compare.

The first time this is easy. It gets interesting when you change one thing at a time: send faster, use more colours, do not announce when it starts, or send the same colour twice in a row.

Write down what went wrong each time. You will find that you are holding the to-do list for the coming weeks. Everything that annoyed you as a human receiver, your program will have to solve later.

## The numbers do not match

You send (255, 0, 60) to the LED, and the sensor reports completely different values. That is correct, not a bug.

Why it is so and what to do about it is the subject of [Challenge 1](challenge-1.md). Leave the question open until then.

## If you finish early

Try different colours and write down what the sensor reports for each. Change the distance and watch what happens to the numbers. These notes will be useful in Challenge 1 straight away.
