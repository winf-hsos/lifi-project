# Challenge 3: The Listener

Online: <https://docs.lifi-project.de/challenges/challenge-3.html>

Until now a human has helped you. Somebody started both programs shortly after each other, and so it was clear when things begin. That help is gone now.

> **Can your receiver find the beginning and the end of a message all by itself?**

It is running before the sender starts. It listens into nothing, sees readings all the time, and has to work out on its own which of them mean something and which are just the room. And when the message is over, it has to notice that too, because it does not know in advance how long the message is.

## The task

The receiver is started and waits. Some time later, the sender begins. The message can be of any length, and its length is not known to the receiver beforehand.

At the end the complete message is on the screen, and the receiver knows that it is complete.

## What is new

**Framing.** An agreed pattern at the beginning says "here we go", another one at the end says that it is over.

**Synchronisation.** The starting pattern can at the same time be used to adjust your clock to the other side's.

**A program with memory.** Your receiver has to know what state it is in: still waiting, reading right now, or done? The same reading has to be handled differently depending on that state.

## Halfway through: the interop test

In the middle of this challenge you swap your **protocol specification** with another team. Each team then builds a receiver for the other team's method.

This is not a chore. It is the only honest test of your documentation. An agreement that works between the two of you because you silently fill in the missing parts is not a protocol yet. Where something is missing, you only notice when somebody else has to work from it.

If you are working on your own, hand your specification to somebody who has not seen your code, or to an AI assistant in a fresh session, and ask them to describe the receiver they would build. The gaps show up just the same.

## At the end: the standards meeting

To close this challenge, the whole class agrees on **one** shared frame. Not one we thought up for you, but one drawn from your proposals.

Whose preamble was more robust? Who had thought of a length field and who had not? Where exactly did the receiver for the foreign protocol fail? From these experiences comes the standard everyone works with from [Challenge 4](challenge-4.md) on.

One thing to settle there goes beyond your protocols so far: which **file types** should the standard know, and how many bits does the field get in which the type is stored? In Challenge 4 the receiver has to know whether the bytes that arrived are a picture or a text, in order to display them.

This is how real standards come about, by the way: not on a drawing board, but by trying different solutions, comparing them, and then agreeing on one. A standard is an agreement between people, not a technical necessity.

The order matters. First you invent for yourselves, then you notice what is missing, and **after that** comes the standard. Had we given you the frame right away, you would not have discovered anything, only implemented it.

What you do **not** give up: everything below the bit stream. How bits become light stays your own method, standard or not.

## What is measured

**Correctness without human help.** The receiver is already running, the moment of sending is decided from outside, and the message has to arrive complete and correct.

The interop test is looked at separately: how many teams were able to work from your specification?

## Showing it works

You start your receiver. Somebody else decides when the sender starts, and you do not know in advance when that will be.

Live change: "Now transmit two messages one after the other, without restarting the receiver."

## What you hand in

- **Your protocol specification.** Complete enough that another team can build a receiver from it. It is also what you pass on in the interop test.
- A short report on the interop test: what was missing in the other protocol, what was missing in yours?
- Your log of mistakes

## Concepts you need

- [Protocols](../concepts/protocols.md)
- [Sampling and synchronisation](../concepts/sampling-and-synchronization.md)
- [Algorithms and programs](../concepts/algorithms-and-programs.md)
- [Abstraction and layers](../concepts/abstraction-and-layers.md)

## A tip that saves you a lot of time

In your code, separate the question "which bits do I send" from the question "how do I turn bits into light". Once these two parts are separate, you can temporarily replace the lower half with something simple: the sender writes its bits into a file, the receiver reads them from there.

That way you can develop and try out your whole framing logic without any hardware connected, and without waiting minutes for a transmission. And when something does not work, you know at once whether it is your logic or your optics.

This separation pays off twice in Challenge 4, because there it becomes a requirement.

## Traps we know about

**The receiver starts on noise.** If your starting pattern is too short or too inconspicuous, the receiver takes some random fluctuation for the beginning of a message.

**The starting pattern appears inside the data.** If your preamble can by chance also occur as part of a message, the receiver starts over in the middle. This problem is real and has a name in practice, but the solution is yours to find.

**The end is not recognised.** The receiver keeps reading and chokes on whatever comes after.

**The specification describes only what you built.** It has to describe what somebody would have to build who does not know you. That is a difference you only notice when it is too late.

## If you finish early

Build the timing information into every symbol instead of setting it only once at the start. Then your receiver can keep readjusting itself, and long messages no longer drift apart. With that you are technically close to what real transmission methods do.
