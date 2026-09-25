<!-- Lecture notes for the slides on `abstraction-and-layers`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/abstraction-and-layers.html -->

# Lecture notes: what's under the switch? (Abstraction and Layers)

This text explains the input on the concept "Abstraction and Layers" for reading afterwards. It follows the order of the slides, and the references count frames (every build-up step is a frame of its own), but it can also be read without the slides.

The deck has no slot of its own in the semester plan. Parts 1 and 4 belong at the end of session 7, after the input on sampling and synchronization; parts 2 and 3 carry the review in session 14. No slide assumes at which point in the semester it is shown, and the deck works in week 7 just as well as in week 14. If you read it in one go, you have the whole concept.

## The switch (Frame 4)

This morning each of you pressed a light switch. Between your finger and the lamp there are a power station, a grid across the whole country, a transformer in the street and a wire in the wall. You knew none of that at the moment, and none of it was missing.

That is not a gap in your education. It is the reason you can turn on a light at all without being an electrical engineer.

## What the switch promises (Frames 5 to 7)

Behind the switch hangs a chain: wire, transformer, grid, power station. For using the switch, this chain is completely invisible. The switch promises exactly two things, up and down, and it keeps that promise no matter what happens behind it.

That is exactly why the power supply of a whole country can be rebuilt, from coal to wind, without anyone having to learn a new switch. What lies behind the promise may change. The promise stays.

## The word for it (Frame 8)

**An abstraction hides how something works and shows what you can do with it.** The second half of the sentence is the more important one. An abstraction does not only hide, it also provides something, and this provided part is called the **interface**.

An interface is a promise: as long as you keep to it, it works. With the switch, the whole promise consists of two positions.

## Three you have already used today (Frame 9)

There is not a single line in this project that does not rest on several such promises.

`led.set_color(255, 0, 0)` hides USB, the Tinkerforge protocol, voltages and the driver of the diode. Three numbers in, light out. `python` hides machine code, memory and the processor. `photo.jpg` hides bytes on a disk, a file system and a controller.

`set_color` is the light switch of this course. If you had to think about USB packets at every call, you would never get to a challenge.

## Your own stack (Frames 11 to 16)

Now the change of perspective: you do not only use abstractions, you build some yourselves, roughly one per challenge.

Take a photo and send it across the link. From top to bottom it looks like this:

| Layer | What lies at this level |
| --- | --- |
| meaning | the photo |
| code system | the bytes of the file, `FF D8 FF E0 …` |
| frame | preamble, type, length, payload, checksum, end |
| bits | `1101 0010 0110 1001` |
| symbols | four distinguishable colours |
| carrier | light |

Read from the top, it is a photo. Read from the bottom, it is a diode going on and off. In between lies everything this course is about.

## The one rule (Frame 17)

**Each layer talks only to the one directly below it.** This one rule sounds harmless and is the reason for everything that comes after it: interchangeability, division of labour in the team, and a search for errors that does not poke around in the fog.

## What the separation buys you (Frame 18)

Your function that translates text into bits knows nothing about colours. Your colour recognition knows nothing about letters. The only thing both know is the bit stream between them, and exactly that is their interface.

The most common misconception is that this is about tidiness. It is insurance: whoever changes the colour assignment cannot break the text encoding along the way, because they do not even touch it.

## Who may drive the LED? (Frames 19 to 21)

Three functions, three layers: `send_text()`, `send_frame()`, `send_symbols()`. Which of them may call `led.set_color()`?

The question sounds like a property of the functions, but it is a question about a **call**. That is why the answer on the slide is on the arrow and not on the box.

The green arrow is allowed: `send_symbols()` may. It is the lowest of the three, and only there is it known at all which colour a symbol carries. The other two do not know it and should not know it.

The red arrow is the shortcut from the very top straight to the very bottom that everyone takes once when things have to be quick. Its price comes due later: whoever takes it has set the colours in concrete inside `send_text` and can no longer change the alphabet without touching the text code.

## Swapping the bottom layer (Frames 23 and 24)

Now the test of whether the separation really holds. Replace the LED with a loudspeaker and the colour sensor with a microphone. What has to change?

Above the symbol layer, not a single line. Five layers stay unchanged, one is exchanged. We do not rebuild this in the course; as a thought experiment it is enough, and whoever has separated the layers cleanly could do it in an afternoon.

**The same bits, three carriers.** The thought behind the swap is bigger than the swap. Information always needs something physical to carry it: a colour on the LED, a voltage on a wire, a tone from the loudspeaker, the magnetisation on a hard disk. But it is not that physical thing, and it does not depend on it. The same bit stream you send through light could run through a cable or over a loudspeaker, and everything above the lowest layer would not notice. That is exactly why there is a discipline of its own for information and not just electrical engineering; outside computer science the same idea is called substrate independence. What you send is the bits. Light is just what carries them today.

Honesty demands the other half: the achievable symbol rate does change. Everything keeps running, but at a different speed. An abstraction makes the swap possible; it does not make it free of consequences.

## Extending the alphabet (Frames 25 and 26)

A team goes from four colours to eight. Which parts have to change?

The answer is in the same stack as everywhere else: only the symbol layer is yellow, and next to it is what lies inside it, namely the colour table, the calibration and the translation between bits and symbols. Every other layer stays as it is.

The tempting wrong answer is "all layers, because each symbol now carries more bits". But the bit stream is the same bit stream; it is only spread over colours differently. And the receiver does not learn the number of colours from the frame, but because it belongs to the same team.

## Why the frame says nothing about time (Frame 27)

A frame is defined **in bits**, not in colours, and it says nothing about time.

That is not an oversight. Timing is a property of the transmission path, not of the message. If the frame contained a field "symbols per second", swapping the substrate would no longer be clean, because sound tolerates a different rate than light. If the class standard is already in place, this is the confirmation; if it is still to come, it is the brief for the standards session.

## The reversal (Frames 28 and 29)

Everything in this project sits on light. And light is the one layer you could replace.

The course is not called light communication. It is about how information is represented, how you break a problem into testable parts, how you build something bigger than your own head, and how you work with an assistant that will claim anything. Light is the object on which all of this can be shown.

## What layers cost (Frames 31 to 33)

So that this does not turn into a doctrine of salvation: layers have a price.

**Every layer adds its own data.** The frame costs bytes that are no longer available for the payload.

**Every boundary hides a knob.** And reliably it is the one you want to turn right now.

**You have to know where the boundaries run.** Guess them wrong and you search in the wrong place.

The answer "there is no price" is wrong. Layers cost throughput and direct access. They are still right most of the time, but that is a trade-off and not a law of nature.

## Narrowing down the fault layer by layer (Frames 34 to 36)

Wrong letters arrive at one team. A test shows that the colour recognition delivers the transmitted symbols one hundred per cent correctly. Where do you look first?

Above the symbol layer. The reflex goes to the sensor, because that is where the mysterious part sits, but the test has cleared the lower layer. That halves the search without anything having been repaired.

This is the same approach as in session 1, only applied to a defect instead of a task: split it up, test the parts one at a time, put the tested part aside. **A tested layer is a layer you can stop suspecting.**

## How to test a single layer (Frame 37)

You give it a known input, look at its output and leave out everything below it. Bits in, bits out. No LED, no sensor, no room light.

That way the translation from text to bits can be checked at your desk, in a second instead of in a whole run. Once you have done that, you will never again spend an hour at the sensor looking for a mistake that sits in a loop.

## Why our module does not hide everything (Frame 38)

`lifi_hardware` hides USB, the Tinkerforge protocol, voltages and the driver. Two things it shows openly: **integration time** and **gain**.

That is intentional. These two knobs are the trade-off only you can decide, and you decide it with a measurement series. An abstraction that takes the deciding question off your hands takes away the work you are here for.

**A good interface hides what you don't need and shows what you must decide.** On top of that it is small and stable: the machinery underneath may change without anyone above noticing. An interface that offers a separate function for every special case is not a good one, only a large one.

## To finish (Frame 39)

You now know what lies under a switch. And every layer you write yourselves is one too: narrow from the outside, big on the inside, and built that way on purpose.
