# The Goal

Online: <https://docs.lifi-project.de/index.html>

Somewhere on your laptop there is a photo. Maybe of a dog, maybe of last summer. Now imagine you had to get that photo to the laptop next to you, and the only thing you were allowed to use was a small lamp and a light sensor. No cable, no Wi-Fi, no USB stick. Just light.

That is what you will build this semester: a device that sends a file from one computer to another by blinking. Two of them stand on the table, facing each other, a hand's width apart. One blinks, the other watches. At the end of the semester a picture will travel across that gap.

I should tell you right away that this module is not about sending pictures with light. Nobody needs that. The lamp is a trick, and this page explains what the trick is for.

## What the lamp is for

A computer is a strange thing to learn about, because everything interesting in it is invisible. It happens inside chips, in millionths of a second, behind layers of software that somebody else wrote. You can use a computer for a lifetime without ever seeing what it actually does with your photo.

The device you build pulls one small piece of that into the open. It sits in front of you and blinks. You can put your hand in the way and watch what goes wrong. What happens inside a computer millions of times a second, unnoticed, happens here a few times a second, and you built it yourself.

That is the whole idea. Everything the module wants to teach you can be seen on that table.

## The question behind everything

This module has one big question, and every week is a piece of the answer: **how can we solve complex problems with computers?**

To answer it you need to understand what a computer does with information, and there are four things it does. It represents information, it stores it, it transfers it, and it processes it. Those four verbs are the four parts of the [map of the module](concepts/index.md), and your device touches all of them.

**Representing.** To a computer your photo is not a picture. It is a list of numbers. And the numbers are not numbers either, they are states of something physical: a voltage, a magnetised spot, a flash of light. When your file crosses the gap, you will have built that whole chain yourself, from meaning down to the lamp and back up to meaning. On the way you will meet the border where an endlessly smooth world is cut into a handful of separate states. That same chain is in every computer, every hard disk and every cable. Once you have built it once, you will recognise it everywhere.

**Storing.** The photo has to sit somewhere before it is sent and somewhere after it arrives. You will open a file and look at its bytes one by one, change one, and watch the picture obey. After that a file is no longer a mysterious icon.

**Transferring.** This is where the lamp does most of its work. The receiver does not know when a letter begins and when it ends. It does not even know whether anyone is sending. The light it sees is never quite the light that was sent. Every trick that makes the link faster makes it less reliable. All of this is true for Wi-Fi and for undersea cables too, but there it happens too fast to watch. Here you can watch.

**Processing.** Somewhere a computer has to turn the numbers that arrive back into a picture, check whether they arrived correctly, and decide what to do if they did not. That is done with a surprisingly small toolbox of logic, and you will see how far that toolbox reaches.

## What you will actually learn

The four verbs are the content. But the reason I teach this module is what you learn while getting the device to work, and that is not about lamps at all.

**How to make a computer do what you mean.** A computer is stubborn. It does what is written, not what was meant. Programming is, more than anything, the craft of stating an intention so precisely that nothing is left open. You do not learn that by listening. You learn it by trying, failing, and finding the mistake. You will do a lot of that, and you will get good at it.

**How to cut a big problem into pieces you can test.** "Send a file with light" is not a task you can solve in one go. You will have to break it down until every piece is small enough to check on its own. And you will learn what happens when the pieces are too big: nothing works, and you cannot tell why. Of everything in this module, this skill is the one you will use most in the rest of your studies.

**How to find out what is true.** Your AI assistant will tell you that eight colours are a good alphabet for your device. Is that right? There is only one honest way to find out, and it is an experiment. You will make guesses and test them with measurements. You will measure before a change and after it, because otherwise you cannot know whether the change did anything. And then comes the second half, which is the engineer's half: the measurements do not decide for you. At some point you have to commit to a solution although several would work and none is perfect, and afterwards you have to be able to say why you chose this one.

**How to work with an AI assistant.** You work with AI support from the first day, and I want you to. Not only for programming. Let it explain what you did not understand in class. Ask it for ideas when you are stuck and for feedback when you are unsure. Use it to look up what you need to know about your parts. An assistant is patient, always there, and never thinks a question is too simple.

The interesting part is where it stops. It knows nothing about your device. How far your link reaches and how fast it can go, it can only guess. You can measure it. Telling apart a suggestion that really helps from one that merely sounds plausible is a skill you will need in every subject from now on, and this is the place to practise it, because here the lamp always has the last word.

## Why light, of all things

Because you can see it. The questions above need some path for information to travel from one place to another. A cable would do, but it would hide everything interesting. With light you can watch.

Because light is analog and a computer is not. Light can be any brightness at all. There are no steps, and between any two brightnesses there are always infinitely many more. The whole rest of the world is built like that: temperatures, sounds, distances, colours. A computer, on the other hand, knows only a limited number of clearly separated states. For it to deal with the world at all, somebody in between has to decide which of the infinitely many shades will from now on count as the same state. Here that somebody is you, and you feel the consequences at once. Choose a few brightnesses, far apart, and your message survives even when the signal wobbles. Choose many, and you get faster, but a small disturbance turns one letter into another. Why digital technology can be reliable although the world is not, you will not learn here as a claim. You will learn it as your own measurement.

And because light is awkward enough that the problems are real. The sensor reports numbers, not colours, and they are never the numbers you sent. The two devices share no clock. Every setting that buys speed costs certainty. None of this is a bug in the kit. It is what every real communication link has to deal with, shrunk to a size that fits on a desk.

## How you get there

Five challenges. In each one, every team competes under the same conditions.

| | Challenge | What it is about |
|---|---|---|
| [0](challenges/challenge-0.md) | The Spark | get the hardware running, first lines of Python |
| [1](challenges/challenge-1.md) | The Alphabet | how many states can you tell apart reliably? |
| [2](challenges/challenge-2.md) | The Word | coding and timing |
| [3](challenges/challenge-3.md) | The Listener | synchronisation without a start signal |
| [4](challenges/challenge-4.md) | The Packet | everything together, as fast as you can |

Each challenge adds exactly one new difficulty, and everything else stays as you already know it. So you never have to master everything at once. What you measured in Challenge 1 you keep using in Challenge 2. What worked in Challenge 2 carries you through Challenge 3. At the end stands a task that looks impossible today, and you will solve it with tools you built for yourself, piece by piece, along the way.

## Where you start

At the very beginning. That you have never programmed is not an obstacle here. It is the assumption I plan with. The first three weeks are there for one purpose only: your LED lights up and your sensor prints numbers. Nothing is graded.

You will get stuck along the way. That is part of it and not a sign that you are in the wrong degree programme. You work in pairs, you have an assistant that answers at three in the morning, and you have me.

The competition is nothing to be afraid of either. Its ranking does not count towards your grade. What counts is the exam at the end, and it is about the [concepts](concepts/index.md) of this module, the same ones you will have come to understand hands-on, while getting your own device to work. You will have to prepare for it, but you will not start from zero: by then you will have met every one of these concepts in practice.

## What stays with you

You will probably never touch the device again after the semester. The questions behind it, though, will keep coming back: how is something represented digitally? Why does information get lost on the way? How do I cut a problem so that I can solve it? And when can I trust an answer I did not check myself?

If at the end of the semester you say this was a module about sending light, then I have done something wrong.

Ready? Here is where to go next:

- [Overview](concepts/index.md): the map of the module, the concepts, the challenges and what they need
- [The Project](challenges/index.md): the device, your partner, the tools, what every challenge produces
- [Required Software](software/index.md): what to install, step by step
- [Hardware](hardware/index.md): the parts and the case
- [Working with your AI assistant](ai/index.md)
