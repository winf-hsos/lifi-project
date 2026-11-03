# Challenge 1: The Alphabet

Online: <https://docs.lifi-project.de/challenges/challenge-1.html>

Challenge 1 is now maintained on Hands-on Computer Science (Challenge 1: English <https://hands-on-computer-science.de/cs/en/items/lifi-challenge-1/>, German <https://hands-on-computer-science.de/cs/de/items/lifi-challenge-1/>). The text below is the last version from the course website; where it disagrees with Hands-on Computer Science, Hands-on Computer Science is right.

This challenge looks harmless, and it decides your whole project anyway. It asks a single question:

> **How many different states can you tell apart, without a single mistake, over 20 attempts?**

Here is why it matters. Whoever can reliably distinguish four states will later send two bits per symbol. Whoever manages sixteen sends four. At the same speed that is twice the throughput, and twice the throughput is what wins the final.

## The task

The sender shows a colour from a set that you define yourselves. The receiver says which one it was.

No timing and no message: the test (`run_test` in `lifi_hardware`) shows one colour at a time, waits until the receiver has measured, and only then shows the next. Everything goes into one file, `alphabet.py`, with your colours, `calibrate`, `send_symbol` and `receive_symbol`. It works with both devices on one laptop and with one device on each of two laptops; the details are in the README of the template.

The two boxes of sender and receiver touch wall to wall, the same for everyone.

## What is new

For the first time you have to **find something out** about your setup instead of thinking it up. How many states can be told apart, nobody knows in advance, and neither does the AI assistant. It depends on your sensor, your distance, your room, and whatever you build in between.

## Start with the human

Before you write a line of code, do the measurement once with your eyes. How many colours can **you** reliably tell apart when you see them one at a time, not side by side?

Write that number down. It is a useful reference, and it will surprise you. In some respects your eye beats the sensor by a wide margin, in others it loses clearly.

One of the reasons matters for the rest of this challenge: your visual system recalibrates itself all the time. When the light in the room changes, you hardly notice, because your brain corrects for it. The sensor does not. It simply reports different numbers.

## Required: the control measurement

You measure **twice**:

1. **Without any aids.** Bare LED, bare sensor, the fixed distance. How many states can you manage like this?
2. **With your setup.** Build your light channel, a tube, a shade, whatever you come up with, and measure again.

Only the second, better value counts. Both measurements belong in your documentation, though. Without the first one you cannot know whether your setup made any difference at all, and that is exactly the point.

What you may build is described under [optical setup](../hardware/index.md#optical-setup).

## What is measured

The size of your alphabet, meaning the number of states you can tell apart over **20 attempts without error**. A single mistake counts as a fail for that alphabet size. The sequence of the 20 attempts comes fresh from the course server for every run, and every run appears in your team cockpit.

So it does not pay to gamble. Eight states recognised reliably are worth more than sixteen with an occasional mix-up.

## Showing it works

At your own place. You run the test yourselves; Nicolas comes round, looks at your setup and checks the result. Then one live change, for example: "Add one more state. Does the hit rate hold?"

## What to keep

Documentation is optional and only for your team: nobody grades it, and the bonus depends only on passing the challenges. Keeping it pays off anyway, because every later challenge builds on it:

- The measurement log of the control measurement without aids
- The measurement log with your setup
- A photo of your optical setup with a short explanation of why you built it that way
- Your log of mistakes (see [Working with your AI assistant](../ai/index.md))

## Concepts you need

- [Analog and digital](../concepts/analog-and-digital.md)
- [Symbols and information](../concepts/symbols-and-information.md)
- [Signal and noise](../concepts/signal-and-noise.md)
- [Measuring and Experimenting](../concepts/measurement-and-experiments.md)
- [Algorithms and programs](../concepts/algorithms-and-programs.md)

## Traps we know about

**Fixed thresholds.** The obvious first attempt is "if the red value is above 500, it was red". That works on Tuesday and fails on Thursday, because the ambient light has changed. Whoever notices this arrives at calibration, and that is the strongest result this challenge has to offer.

**Looking only at R, G and B.** The sensor delivers four values. The fourth, the clear channel, is more sensitive than the other three. Ignoring it throws away signal.

**Too few repetitions.** If you test each state three times and see no error, you know nothing yet. Only over many attempts does it show whether two states are really cleanly separated.

**Pretty colours instead of distinguishable colours.** Sixteen colours that look different to your eye are not necessarily different to the sensor.

## If you finish early

Change the integration time of the sensor and measure what happens to your numbers. You will find that longer measurements are calmer but allow fewer measurements per second. This trade-off will decide your throughput in Challenge 4.
