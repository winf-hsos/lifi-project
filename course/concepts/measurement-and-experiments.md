# Measuring and Experimenting

Online: <https://docs.lifi-project.de/concepts/measurement-and-experiments.html>

## Summary

Whether a real setup behaves the way you expect can only be decided by measuring it. An experiment that tells you something changes conditions on purpose, repeats readings, and records what was done and what came out. This concept is the craft of the module: it applies to every claim about your setup, not only to light. What those measurements then say about the limits of your link, how many colours you can safely tell apart, is the subject of [Signal und Rauschen](signal-and-noise.md).

In this chapter, we address the following questions:

- Why is thinking not enough to know how my setup behaves?
- What does the colour sensor actually deliver, and why does it not match what was sent?
- What belongs to a measurement series that really shows something?
- What is a control reading for?
- What do integration time and gain do, and where is the trade-off?
- How often do I have to repeat before a lucky hit stands out?
- How do I record what I measured?

You need this concept by [Challenge 1](../challenges/challenge-1.md) at the latest, and you use it in every challenge after that.

## Explanation

You can know almost nothing about your setup without measuring it. Whether a change actually helped is not answered by thinking, by a gut feeling, or by an AI assistant, but by a trial. For two thousand years people believed Aristotle, that heavy bodies fall faster than light ones. As the story goes, two balls dropped from the leaning tower of Pisa were enough to end the error. Your setup is your tower. The assistant knows sensors of this kind, but only a measurement knows yours.

### What the sensor actually delivers

The colour sensor does not return three values, it returns four: the filtered shares of red, green and blue, plus **clear**, measured without a colour filter. Clear sees all the incoming light and is therefore more sensitive than the colour channels. When you separate bright from dark, it is your most useful value.

[Figure: One reading, four numbers. Clear has no colour filter, which makes it the most sensitive of the four.]

And none of these values matches the numbers the sender gives its LED. Send `(255, 0, 0)` and the sensor measures something like `r=203, g=41, b=57`. The colour filters overlap, the distance swallows light, and the room light is always measured too. That is not a defect, it is the normal case. The consequence: you do not calculate backwards to what was sent, because a formula that fits today will not fit tomorrow. You **measure how each transmitted colour arrives at your end**, and you assign every new reading to the closest pattern you learned. Calibrate, then classify: that is the core of Challenge 1.

[Figure: Calibration as a picture: the red and the blue readings as clouds in a coordinate system of red and blue share, with green roughly constant here. A new reading is assigned to the nearer cloud.]

### One reading is a draw

Measure the same red LED five times and you get five different values, say 198, 205, 201, 195, 206. None of them is "the true one". Every real measurement scatters; noise is the normal case. A single reading jumps around, an average sits still. If you need a stable value, read several times and take the mean.

[Figure: The same light, read individually and as averages of five. The individual readings scatter widely, the averages huddle around the centre. Both series have the same mean.]

You can try that yourself in [the noisy sensor](https://winf-hsos.github.io/lifi-concept-demos/noisy-sensor/). A sender there transmits one of two symbols, led off or led on, and the receiver decides at a threshold which one arrived. The same readings decide three times side by side: alone, averaged over five, averaged over ten. Send twenty-five symbols and the single readings put a few dots on the wrong side of the threshold, while the averaged ones no longer reach it. The price stands next to it: the same number of decisions costs five or ten times as many readings, and the symbol rate drops from twenty per second to four or two. Which of those you need is not a matter of taste, it depends on your own setup: with little noise a single reading already decides correctly every time, with much noise even the average of five slips occasionally.

Interactive demonstrator: <https://winf-hsos.github.io/lifi-concept-demos/noisy-sensor/>

There is a second reason to measure more than once. The sensor never reads zero, because room light is always there. So every measurement series starts with a **control reading**, with your own LED switched off. That is the zero point you read every colour measurement against, and it tells you when the surroundings change, through afternoon sun or the LED of the team next to you.

[Figure: Measure the dark first. What the LED adds is the difference to the ambient level, and every reading carries ambient light and noise with it.]

### The trade-off: integration time

The **integration time** is the sensor's reading window: it decides over how much light a single value is averaged. Long windows give calm values but few readings per second. Short windows give many readings but shaky values, until single readings slide into the wrong range and a red is read as a blue. (**Gain** is the second knob; it scales the values and carries a related trade-off.)

[Figure: The same second, read three times over. Every bar is one reading and its width is the window it averages over: four long ones fit into the second, or twelve short ones. The shorter the window, the more readings you get, and the more they scatter, until single ones land outside the band that still reads correctly.]

Longer is calmer, shorter is faster. That is the central trade-off of the whole project, because the symbol rate of your transmission hangs on it. Where the limit of your setup lies is answered by no table and no assistant, only by your own measurement series. Here you meet the knob; what its setting means for your alphabet and your throughput is worked out in [Signal und Rauschen](signal-and-noise.md) after the first challenge.

### Measuring on purpose

A **measurement series** is several readings under equal, recorded conditions, in which at most one quantity is changed on purpose. Every word carries weight. Whoever changes two things at once, say distance and integration time, and gets a better result, knows only **that** it got better, not what did it. Whoever does not write the expectation down **beforehand** can read almost any result as a success afterwards. And the record needs the conditions, the changed quantity, the number of repetitions and all the values, including the uncomfortable ones: outliers are often the most interesting information.

[Figure: What makes a measurement series: write the conditions and the expectation before, change one variable and repeat during, keep every value and compare with the expectation after.]

Repetitions are not decoration, they are your protection against a lucky hit. With two colours, pure guessing gets every second one right; five in a row succeed by chance about once in 32 attempts. Fifty out of fifty essentially never happens by luck. That is exactly why the acceptance tests in the challenges are cut to long series.

And when a clean measurement series contradicts a suggestion from the assistant, the series wins. Check briefly whether it really was clean, one variable, enough repetitions, a control reading, and then the case belongs in your log of mistakes: suggestion, measurement, outcome. Put shortly: what you did not measure, you do not know.

## Slides

The slides for this concept, right here. Page through them with the buttons in the top right corner, or click into the slides and use the arrow keys. The other buttons give you full screen, the slides in a new tab, and the deck as a PDF.

## Practice questions

Try questions in the exam format here, with the answer and its reasoning shown right away.

## Further reading

- Richard Feynman: Cargo Cult Science. Caltech commencement address, 1974, freely available [online](https://calteches.library.caltech.edu/51/2/CargoCult.pdf). Six pages on the one habit that makes an experiment worth anything: reporting everything that could make your own result wrong. "The first principle is that you must not fool yourself, and you are the easiest person to fool."
- David J. Hand: Measurement. A Very Short Introduction. Oxford University Press, 2016. What a measurement actually is, why every value carries a scale and an error, and how measurements get compared. Short, readable, and useful far beyond sensors.
