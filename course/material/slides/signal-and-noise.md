<!-- Lecture notes for the slides on `signal-and-noise`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/signal-and-noise.html -->

# Lecture notes: why 16 and not 4? (Signal and Noise)

These notes explain the contents of the deck `index.html` for reading afterwards. They follow the order of the slides; references such as "(Frame 9)" point to the number the deck shows in the bottom right corner, and build-up steps count separately. The matching concept on the website: [Signal and Noise](../../website/concepts/signal-and-noise.qmd).

## What it is about

How much your link carries is not decided by your code. It is decided by the ratio of the distance between the symbols to the scatter of the readings, and every measure against it has a price you should know before you pay it.

The deck runs in session 5, right after the competition for Challenge 1, and the first slide picks up your fresh results. It is still a **normal input** and stands on its own: if you go through it alone later, you need neither the ranking on the wall nor the lecture hall. **Two slides are filled in during the session** (Frame 5 and Frame 24). They come pre-filled, so that they still say something when you read them afterwards, and because the deck is HTML you really can type into them.

## Part 1: what your data says

**The lighthouse in the fog (Frame 4).** The lamp burns exactly as brightly as on a clear night, and yet the beam dies after a few metres. Nothing has happened to the signal. Something has happened to everything else. That is exactly your situation after the competition: all teams had the same LED, the same sensor, the same room, all senders were equally bright, and still one team gets 16 colours through and another gets 4.

**Your results (Frame 5).** Team, alphabet size, hit rate, and what was done against the noise. The last column is the most important one; filling it in turns it into the answer itself. First collect, do not comment; then ask the question and let it stand: same hardware, same task, a factor of four between first and last. Where does the difference come from?

**Ten readings of one colour (Frames 6 to 8).** Point the sensor at one colour and read it ten times, without changing anything. You get ten different numbers. That surprises most people, because a computer is the one machine that reliably gives the same output for the same input. But the sensor never gets the same input twice: the light flickers, the electronics hiss, someone walks past the window. This variation is called **noise**, and every measuring instrument in the world has it.

In the third step the same ten values lie on a number line, and you can see what is left of them: a spread from 207 to 220. From this follows something that carries the whole session: **a single reading says almost nothing.** The value 220 could be this colour, or a neighbouring colour in a bad moment. Only the ten together tell you where the colour really sits and how far it wanders.

**Not the code, the scatter (Frame 9).** The punchline comes early, and the evidence follows. That the quality of the programming decides almost nothing here surprises most people; that is exactly the point. Noise is not a defect and not a bug, it is a property of every measurement, and whoever makes it smaller fits in more symbols.

## Part 2: what decides your alphabet

**The same signal, measured differently (Frames 11 to 14).** There is a way to make the numbers calmer, and you already have it: measure for longer and average what arrives. At the top the raw signal as it arrives at the sensor, far too restless for a decision in a single instant. Below it the same signal, averaged over windows of 4, 12 and 32 readings; every thick bar is one value, and the bars settle closer and closer to the true level.

But the place to look is the right-hand edge. The same stretch of time holds 288 raw values, then 72, then 24, then 9. **Calmness is not free, you pay for it in readings per second**, and readings per second are exactly what your speed is made of. That is the first price tag of this input, and not the last.

**Two symbols, two clouds (Frames 15 and 16).** Now two symbols on the same scale. Each one is not a single value but a cloud of values, and the width of that cloud is the noise from before. On the left the clouds are narrow, the boundary between them lies in empty space, and every reading lands on its own side. On the right the distance is the same, but the clouds are wider, and the parts that reach across the boundary are exactly the readings the receiver assigns wrongly. Neither the distance nor the width decides on its own.

**The ratio is what counts (Frame 17).** The quantity this whole input is about is a quotient: the distance `d` between two symbols, divided by the spread `s` of the readings. Your alphabet size measures nothing else, and that is why it explains the table from the beginning.

From this follows a sharper version of a phrase we have used loosely up to here. **Safely distinguishable** does not mean that the means are different. It means that the clouds do not overlap, not even at their outermost values. A single reading that slips across the boundary is a wrong symbol, and one wrong symbol in fifty runs costs you an alphabet size. If you document a colour only by its mean, you do not yet know whether it is usable.

**How many symbols fit? (Frame 18).** As soon as you think in bands instead of points, "how many colours can we use?" stops being a matter of trial and error and becomes a calculation. Measure the usable range of your link, from the darkest to the brightest value you can produce reliably. Measure the width of one cloud. Divide, and you have the number of symbols.

An example to work through: the range runs from 40 to 840, so 800 units. Every colour scatters around its mean by plus or minus 25, so its band is 50 wide and not 25, because the cloud reaches in both directions. And 800 divided by 50 is 16. That is where an alphabet of 16 symbols comes from, and doing this calculation before trying things out saves you half a session in Challenge 2.

**The demonstrator (Frame 19).** [The Distinguishability Lab](https://winf-hsos.github.io/lifi-concept-demos/distinguishability-lab/) has three sliders: number of symbols, length of the measurement window, speed. Two tasks. First: bring the error rate down to zero and watch the throughput while you do it. Second: press the interference button and see what still holds. The numbers are simulated, the structure is real; your own numbers come from your link and from nowhere else.

## Part 3: what it costs

**The toolbox, with price tags (Frame 21).** There are tools against noise, and hardly any of them are free. On the left you enlarge the distance, on the right you shrink the spread. What stands out is how often the same thing is written on the price tags: fewer bits per symbol, or fewer symbols per second.

Three lines are the exception, and they are the reason optical self-build is allowed in this course: focus the light, shield against ambient light, nail down the geometry. They improve the ratio without you giving anything up for it, and they cost only an afternoon with cardboard. Passive, ten euros at most.

**Averaging is not free (Frame 22).** The most common reflex after this analysis is averaging. `read_stable()` shows how: ten readings, one mean. Ten times calmer values, ten times slower. That is not an argument against averaging, it is an argument for measuring the price instead of assuming it is zero. It is the same bargain as a longer integration time, only at a different place: once in the sensor, once in the program.

**Both roads lead to the same wall (Frame 23).** There are two ways to get more out of the link, and students almost always want both at once. More symbols squeezes the bands together. Faster symbols makes the clouds wider. Both use up the same safety margin, and you only have one. Challenge 2 begins at this wall, and the way through it is not a cleverer program but a number you have measured yourselves.

**An honest sentence (Frame 24).** Two or three teams read out an entry from their log of mistakes, ideally cases where a plausible suggestion from the assistant failed against the measurement. The short version goes into the two lines, which are editable. This is the moment when the log of mistakes shows its purpose: it is what sets this course apart from a programming course.

**The measuring stick in the fog (Frame 25).** Everything in this input is a property of **your** link: your room, your distance, your ambient light. If you calibrate by the window, your values will no longer match at the acceptance test in the darkened part of the room. No language model has access to that, and no reading, however good. Your task is not to defeat the noise; that cannot be done. Your task is to measure it and then decide which alphabet and which speed your link honestly delivers. The fog stays; what you hold in your hand is the yardstick.

## Further reading

The concept page [Signal and Noise](../../website/concepts/signal-and-noise.qmd) sums up the whole thing and contains the same figures. How to measure honestly, that is control measurement, one variable at a time, a log, is covered in [Measuring and Experimenting](../../website/concepts/measurement-and-experiments.qmd); this input uses those measurements instead of explaining them. The other half of the trade-off, the number of symbols for the same measurement time, is covered in [Analog and Digital](../../website/concepts/analog-and-digital.qmd). And what you then do with the alphabet is settled by [Code Systems](../../website/concepts/code-systems.qmd) in the next session.
