# Abstraction and Layers

Online: <https://docs.lifi-project.de/concepts/abstraction-and-layers.html>

## Summary

An abstraction hides how something works and shows what you can do with it. The part it shows you is the interface, and an interface is a promise: as long as you keep to it, what happens underneath may change without breaking anything above. Stack several such promises and you get layers, each one talking only to the one directly below. That is how a system gets bigger than any single person can hold in their head, and it is why you can replace one piece of it without rebuilding the rest.

In this chapter, we address the following questions:

- Why can you use something without knowing how it works?
- What lies under the interface you are working with?
- Why can one layer change without the layer above noticing?
- Why does your information not depend on light, or on any other carrier?
- How do you build a system that is larger than your own head?
- What do layers cost, and when is it worth reaching one level deeper?
- Where do you look first when the wrong letters arrive?

You meet this concept the moment you call your first library function, and you use it in every challenge from [Challenge 2](../challenges/challenge-2.md) onwards. It pays off once more when you look back at your finished system.

## Explanation

This morning you pressed a light switch. Between your finger and the lamp there is a power station, a grid across the country, a transformer in your street and a wire in the wall. You knew none of it, and none of it was missing.

[Figure: The switch promises exactly two things, up and down. Everything to the right of it may be rebuilt from coal to wind without anyone having to learn a new switch.]

That is not a gap in your education. It is the reason you can turn on a light without being an electrical engineer. The switch makes a promise that holds no matter what happens behind it, and the promise is small enough to learn in a second.

### Abstractions you are already standing on

You have not written a single line in this project that does not rest on several such promises.

[Figure: Three you used today without noticing. Each shows you a handle and keeps its machinery to itself.]

`led.set_color(255, 0, 0)` hides USB, the Tinkerforge protocol, voltages and the driver of the diode. Three numbers in, light out. `python` hides machine code, memory and the processor. `photo.jpg` hides bytes on a disk, a file system and a controller. If you had to think about USB packets at every call, you would never get to a challenge.

### The stack in your project

Now turn it around. You do not only use abstractions, you build them, roughly one per challenge. Take a photo and send it across the link:

[Figure: The same photo, read from the top down and from the bottom up. Next to each layer is what actually lies there: the image, the bytes of the file, the frame with its fields, the bit stream, four distinguishable colours, and finally light.]

Read from the top it is a photo. Read from the bottom it is a diode going on and off. Everything this course is about lies in between. And one rule makes the whole arrangement work: **each layer talks only to the one directly below it.**

### Who is allowed to talk to the hardware

That rule sounds like tidiness. It is insurance. Three functions, three layers: which of them may call `led.set_color()`?

[Figure: The question is not about the boxes, it is about a call, so the answer is on the arrow. Only the lowest of the three knows which colour a symbol carries.]

Only `send_symbols()` may. The other two do not know which colour a symbol is, and they should not know. The red arrow is the shortcut everyone takes once when it has to be quick, and its price arrives later: colours are now built into `send_text`, and you cannot change your alphabet without touching the code that turns text into bits.

The same separation cuts the other way too. Your `text_to_bits()` knows nothing about colours, your colour recognition knows nothing about letters, and the only thing they share is the bit stream between them. Whoever changes the colour table cannot break the text encoding, because they never touch it.

### Swapping the bottom layer

Here is the test of whether the separation really holds. Replace the LED with a loudspeaker and the colour sensor with a microphone. What has to change?

[Figure: Five layers unchanged, one exchanged. Above the symbol layer not a single line is different.]

Nothing above the symbol layer. We do not rebuild the device in the course, and we do not need to: whoever has separated the layers cleanly could do it in an afternoon. Honesty demands the other half: the achievable symbol rate does change. Everything keeps working, at a different speed. An abstraction makes the swap possible; it does not make it free of consequences.

A smaller change works the same way. Say you extend your alphabet from four colours to eight:

[Figure: Only the symbol layer changes: the colour table, the calibration and the translation between bits and symbols.]

The tempting wrong answer is "every layer, because each symbol now carries more bits". But the bit stream is the same bit stream; it is only spread over colours differently. Frame and text encoding stay exactly as they were.

This is also why the class standard for [Challenge 4](../challenges/challenge-4.md) defines the frame **in bits** and not in colours, and why it says nothing about time. Timing is a property of the path, not of the message. If the frame carried a field "symbols per second", the swap to sound would no longer be clean, because sound tolerates a different rate than light.

### Information and its carrier

The thought behind the swap is bigger than the swap. Information always needs something physical to carry it: a colour on the LED, a voltage on a wire, a tone from a loudspeaker, the magnetisation on a hard disk. But it is not that physical thing, and it does not depend on it. The same bit stream you send through light could run through a cable or over a loudspeaker, and everything you built above the lowest layer would not notice. That is the whole reason there is a discipline of its own for information and not just electrical engineering. In computing the idea shows up mainly in the layer model of networks: the lowest layer wraps the transmission medium, and nothing above it knows which one it is. Outside computing the same idea goes by the name substrate independence, in the philosophy of mind and in debates about artificial intelligence. What you send is the bits. Light is just what carries them today, and that is the reason this course is not called light communication.

### What layers cost

Layers are not free, and the answer "there is no price" is wrong.

**Every layer adds its own data.** The frame costs bytes that your payload cannot use.

**Every boundary hides a knob**, and reliably it is the one you want to turn. Reaching through a layer means either extending its interface or breaking it.

**You have to know where the boundaries run.** Guess wrong and you go looking in the wrong place.

They are still worth it almost every time. But that is a trade-off, not a law of nature.

### Where to look when it breaks

Which brings us to the most useful thing layers do for you day to day. Wrong letters arrive at the receiver. A test shows that the colour recognition delivers every transmitted symbol correctly. Where do you look first?

[Figure: A tested layer is a layer you can stop suspecting. The search is halved before anything has been repaired.]

Above the symbol layer. The reflex sends everyone to the sensor, because that is where the mysterious part sits, but the test has cleared the lower layer. This is the same move as in [Cutting Problems](problem-decomposition.md), applied to a defect instead of a task: split it, test the parts one at a time, and put the tested part aside.

Testing a single layer means giving it a known input, checking its output, and leaving everything below it out. Bits in, bits out. No LED, no sensor, no room light. Your text-to-bits translation can be checked at your desk in a second, instead of in a full run in a darkened room.

### What makes an interface good

One last question, and it is the one that keeps this from turning into a doctrine. Our module `lifi_hardware` hides USB, the protocol, voltages and the driver. But it shows two things openly:

[Figure: A good interface hides what you do not need and shows what you must decide.]

Integration time and gain are in the interface on purpose. They are the trade-off only you can settle, and only with a measurement series (see [Measuring and Experimenting](measurement-and-experiments.md)). An abstraction that takes the deciding question off your hands takes away the work you are here for.

Beyond that, a good interface is **small and stable**: what lives underneath may change without anyone above noticing. An interface offering a separate function for every conceivable special case is not a good one, it is merely a large one.

## Slides

The slides for this concept, right here. Page through them with the buttons in the top right corner, or click into the slides and use the arrow keys. The other buttons give you full screen, the slides in a new tab, and the deck as a PDF.

## Practice questions

Try questions in the exam format here, with the answer and its reasoning shown right away.

## Further reading

- David Parnas: On the Criteria To Be Used in Decomposing Systems into Modules. Communications of the ACM, 1972, freely available online. Five pages from the year the idea got its name, and still the clearest statement of it: split a system by what each part has to hide, not by the order in which the work happens.
- Brian Kernighan and Rob Pike: The Practice of Programming. Addison-Wesley, 1999. Chapter 4 on interfaces is the practical companion to the above: how big an interface should be, what belongs in it, and what a caller should never have to know.
