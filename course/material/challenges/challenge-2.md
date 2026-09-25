# Challenge 2: The Word

Online: <https://docs.lifi-project.de/challenges/challenge-2.html>

In Challenge 1 you sent single states. Now they become a message.

> **How fast can you get ten characters across without an error?**

For that you need two things that were missing so far: an agreement about which sequence of symbols means which letter, and a shared rhythm in which sending and measuring happen. Both cost time, and both decide how fast you can get.

## The task

A word of ten characters travels from one device to the other and appears on the receiver's screen.

Sender and receiver agree on a fixed symbol rate beforehand, for example one symbol per second. A human gives the starting signal by starting the two programs shortly after each other. So your program does not have to find the beginning on its own yet.

## What is new

**Coding.** A letter has to become a sequence of symbols, and both sides have to use the same rule.

**Timing.** The receiver has to measure at the right moment. If it measures too rarely, it misses symbols. If it measures at the wrong instant, it catches the transition between two colours.

## What is measured

First **correctness**: all ten characters have to be right. A word with one error has not been transmitted.

Then **duration**. Among all correct transmissions, the time from start to the complete word decides.

## Showing it works

At the test table you get a word you have not seen before, and you transmit it live.

Then the live change: "Double your symbol rate. What happens?" This question is meant seriously, and it leads straight into Challenge 3.

## What you hand in

- Your coding table, meaning which sequence of symbols stands for which letter
- A measurement log: at which symbol rates did it work, from which one on did it not?
- Your log of mistakes

## Concepts you need

- [Code systems](../concepts/code-systems.md)
- [Sampling and synchronisation](../concepts/sampling-and-synchronization.md)
- [Algorithms and programs](../concepts/algorithms-and-programs.md)
- [Protocols](../concepts/protocols.md), in their simplest form for now

## Traps we know about

**It works at 1 Hz and falls apart at 5 Hz.** This is the central experience of this challenge, and it is intended. Two computers have no shared clock. Over ten characters you do not notice, over a hundred you do.

**Measuring at the moment of the switch.** If the sensor measures exactly while the LED is changing, it delivers values that belong to none of your symbols. A little waiting time after each colour change helps, but costs speed.

**Too many symbols per letter.** If you code every character with eight symbols although your alphabet from Challenge 1 offers sixteen states, you give away more than half of your time.

**The receiver starts too late.** As long as a human gives the starting signal, this can still be fixed by hand. From Challenge 3 on it cannot.

## If you finish early

Ask yourselves whether all letters really have to be coded with the same length. In English text the letter E appears far more often than the letter Q. Whoever codes frequent characters shorter gets faster on average. That is the entrance to [compression](../concepts/compression.md), which counts in Challenge 4.
