<!-- Lecture notes for the slides on `analog-and-digital`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/analog-and-digital.html -->

# Lecture notes: drawing the line (Analog and Digital)

This text explains the input on the concept "Analog and Digital" for you to read afterwards. It follows the order of the slides, and the references count frames (every build-up step is a frame of its own), but you can also read it without the slides.

The deck is the first of two inputs in the same session; the second, [what light means](../symbols-and-information/skript.md), turns distinguishable states into symbols and makes information countable.

## Is this digital? (Frame 4)

A railway station before the age of chips. The split-flap board clatters, letter by letter falling into place. There is no computer anywhere near it, and the thing is nonetheless perfectly digital.

Every flap knows exactly two positions, up or down. While it turns there is no valid state in between, and that is exactly why you can read the board from twenty metres away.

## Digital is not the same as electronic (Frame 5)

The scoreboard from the sports hall that you flip by hand is digital, and so are the light switch, the abacus and the die. The slide rule, the dial thermometer, the dimmer and the hourglass are analog. Not a single one of these things contains a chip.

Electronics is only today's usual carrier, not the defining feature. The reverse holds as well: an amplifier is electronic and still stepless.

## The word for it (Frame 6)

**Digital means finitely many states, and nothing in between counts.** Both halves carry weight. The first is the harmless one; the second is where all the engineering hangs: because nothing between the states counts, every disturbance there disappears as well.

## The part no program controls (Frame 7)

The sender turns numbers into light, the sensor turns light back into numbers: digital, analog, digital. The middle is physics. It is stepless and disturbed by ambient light, distance and noise, and no program in the world controls it.

Whoever forgets this analog middle will later be surprised by every disturbance. Whoever takes it seriously knows why you have to measure.

## Stepless versus states (Frames 8 and 9)

Light is analog: between any two brightnesses lies another, there is no smallest step. Your program needs the opposite, namely finitely many states that are clearly apart.

Digitising a signal means nothing more than representing it by a finite sequence of numbers.

## Same noise, more regions (Frames 10 to 12)

Three times the same measurement with the same wobble, and only the number of regions grows. With two regions the band sits comfortably inside its own region. With four it gets tight. With eight the same band reaches across the boundaries, and individual readings land in the neighbouring region.

The noise did not grow, the margin shrank. The distance between regions is your safety reserve, and more regions spread the same reserve over more boundaries. With that, the competition question of Challenge 1 is posed before anyone asks it.

## What the thrown-away precision buys (Frame 13)

Two copy chains. The tape copies its stepless wave along with all the noise and adds its own with every generation; audibly worse with every copy. The file is born again from clean states at every copy: read, set afresh, done.

Every disturbance smaller than the distance between states disappears completely in the process. That is why digital technology is reliable, not although it throws information away but **because** it does. And that is why the thousandth copy of a file is the original.

## Digitising throws information away (Frame 15)

Which of the infinitely many values inside a region it really was cannot be determined after the assignment. Digitising is a one-way street. That is not an accident, it is the purchase price for everything the previous section showed.

## The two cuts (Frames 16 and 17)

Digitising always takes two cuts, and a photo shows both of them.

The **first cut goes through the area**: the stepless picture becomes measuring points, sixteen by sixteen on the slide. That is **sampling**, and how fine it is is the **resolution**.

The **second cut goes through the value**: the brightness of every point is rounded to one of the agreed steps, four grey levels on the slide. That is **quantization**, and the number of steps is the **colour depth**. Those steps are exactly the regions from before, now applied to a picture.

## Which cut was too coarse? (Frame 18)

Both cuts throw detail away, but they leave different traces, and that is how you tell which knob to turn.

**Blocks** mean too few points, so sampling that is too coarse. **Hard patches in smooth shading** mean too few levels, so quantization that is too coarse. That is worth remembering, it comes back in the workshop.

## What a picture costs (Frame 19)

The one piece of arithmetic that carries every file size: **points × bits per point.** A picture of 64 by 64 points in 24-bit colour is 98,304 bits, so 12 KB. The same picture with one bit per point is 4,096 bits, so 512 bytes.

On your light link, that turns into time straight away. At 30 bit/s the first picture takes almost an hour, the second two minutes. Resolution and colour depth are therefore not fine details but the two levers the transmission time depends on: what you keep, you pay for in minutes.

## How far can you go? (Frames 20 to 23)

The same photo, ever coarser: 128, 32, 8 and finally 2 points per edge. Somewhere in between, recognisability tips over, and where exactly, the room will disagree.

That disagreement is exactly the point. There is no correct amount, there is only a trade-off against the transmission time. In Challenge 4 you have 2 KB, and then this question really comes up.

## Try it yourself (Frame 24)

In [The Photo Digitiser](https://winf-hsos.github.io/lifi-concept-demos/photo-digitiser/) you choose resolution and colour depth yourself, see the result immediately, and next to it the arithmetic including the transmission time over the light link. Two questions are worth asking: at which setting would you still send the picture? And what saves more, half the resolution or half the colour depth?

## The same two cuts for sound (Frame 25)

The two cuts are not a picture topic, they are the method. For sound, the **sampling rate** slices time instead of area, and the **bit depth** slices loudness instead of brightness. 44,100 samples per second at 16 bit: that is a CD.

In [The Audio Digitiser](https://winf-hsos.github.io/lifi-concept-demos/audio-digitiser/) you can hear both: turn the sampling rate down until a voice sounds tinny.

## Where your alphabet is born (Frame 27)

```python
value = sensor.get_clear()

if value > 250:
    symbol = "bright"
else:
    symbol = "dark"
```

This one threshold in the code is the place where hundreds of possible readings turn into two symbols. It is not a constant of nature, it is your decision, and from here on it is the threshold that holds, not the physics.

Where it belongs does not come from your gut but from the profiles of your measurement series: calibrate first, then compare.

## How many colours are safe? (Frames 28 and 29)

Two are safe, eight are fast, and somewhere in between sits your alphabet. Where exactly, only your own measurement series knows: the width of a region has to match the wobble, or individual readings slip into the neighbouring region.

## To close (Frames 30 and 31)

You decide where the lines go. From there on your decision holds, not the physics. Physics delivers a stepless range of values and not a single line with it; every line in your system is there because you wrote it there. That is also why it is your problem when it is in the wrong place.
