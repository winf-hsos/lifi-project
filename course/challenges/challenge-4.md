# Challenge 4: The Packet

Online: <https://docs.lifi-project.de/challenges/challenge-4.html>

Everything you built over the project comes together here.

> **How fast can you get an unknown file onto the other computer, byte for byte?**

For the first time you transmit something whose content you do not know in advance, and for the first time every second counts.

## The task

You get a file of at most 2 KB. You do not know what is in it, and you do not know what kind of file it is. It may be a small picture, a text, or something else from the set of types your class has agreed on.

So your program has to recognise the type from the file, send it along in the header of the transmission, and the receiver has to open the file accordingly at the end.

The file has to arrive **byte for byte**, exactly as it was sent, without a single changed character. The comparison is made with a hash, a checksum over the whole file. Almost right does not count.

That you do not know the content is deliberate. It forces you to transmit truly arbitrary data instead of relying on letters.

## Why only 2 KB

Your channel manages roughly between 10 and 50 bits per second. A kilobyte therefore takes a few minutes, and a real photo would take hours. The limit keeps a run short enough to sit through.

## The shared frame, and what is yours

From this challenge on, the class standard from the standards meeting at the end of [Challenge 3](challenge-3.md) applies. If you are working outside a class, define such a frame for yourselves with the fields below. Either way, your work now splits into two layers.

**Given, the same for everyone, defined in bits:** preamble, a field for the file type, a length field, the payload as bytes, a checksum, an end marker.

**Free, and this is your competitive edge:** how many symbols you use, which colours and brightnesses, integration time and gain, your symbol rate, your calibration method, your timing strategy, your optical setup. In short, everything that turns bits into light and light back into bits.

Because the frame is described in bits and not in symbols, it works unchanged whether you use four symbols or sixteen, and whether you manage two of them per second or twenty.

That is the whole point of the separation: you can swap out the lower layer completely, and everything above keeps running. It is why the same web page arrives over Wi-Fi, fibre and a mobile network. More under [Abstraction and layers](../concepts/abstraction-and-layers.md).

## The type field: data alone means nothing

The same 2000 bytes can be a picture, a text, or noise. What they are is not written in the data itself. It has to be said alongside.

That is what the type field in the header is for. The sender writes there what kind of file it is, and the receiver knows from it what to do with the bytes. Which types exist is decided together at the standards meeting, like the rest of the frame.

The same principle is behind file extensions such as `.png` and `.txt`. They are not in the file either. They stand next to it.

**And then the receiver shows it.** When the transmission is through, your receiver program opens the file the way its type demands: text appears on the screen, a picture is displayed. This is the moment the whole project has been heading for. Light has become numbers, numbers have become bytes, and bytes have become something a human understands again.

To be clear: the hash is still what counts. A damaged picture is often displayed anyway, just distorted. The display is the show, not the proof.

## Nothing in the frame says anything about time

You may notice: there is no field for speed. That is intended.

How fast you send and how the two sides stay together while doing so is a property of your transmission path, not of the message. A transmission by sound would have completely different rules for it. If the speed were in the frame, a solution that does not need it would have to send it along anyway.

So the preamble in the frame is only a bit pattern by which you recognise the beginning. Whether your solution underneath needs its own, slower lead-in is up to you.

## Your decision: how you keep the beat

That leaves the whole question of time with you. How fast you send, how the receiver learns that, and how you prevent the two sides from drifting apart over a long transmission.

The last part is the unpleasant one. Two computers run neither at exactly the same speed nor evenly: wait commands are imprecise, USB sometimes takes longer, the operating system does something else in between. With ten characters you do not notice. With a 2 KB file that is under way for many minutes, it is the most common reason a run fails.

How you deal with it we do **not** prescribe. There are several defensible solutions, they differ in effort and reliability, and which one works best for you depends on your hardware. This is one of the most important design decisions of the whole project, and it is yours.

A tip on how to approach it: first measure how far your two devices drift apart over a thousand symbols. Then you know how big your problem actually is, and you can decide how much effort is worth it.

## What else is new

**Arbitrary data.** Until now you transmitted letters. Now any of the 256 possible byte values can occur, including ones that happen to look like your starting pattern.

**The way back.** Until here everything ran in one direction. From now on the other side may answer. Both devices carry an LED and a sensor, so you can send both ways. That makes possible what was ruled out before: the receiver can confirm that a piece has arrived. It can ask for a broken piece again, specifically, instead of you sending the whole file anew. And both sides can turn the speed up together, as far as it still just works.

You do not have to use the way back. But whoever transmits one-way has to send more carefully, because a single flipped bit makes the whole run worthless.

**Time pressure.** Duration is what is measured.

## What is measured

**The precision run.** If the hash does not match, the run does not count. If it matches, the duration counts.

**The robustness round.** The same run under harder conditions, see below.

**Documentation.** Protocol specification, measurement data, log of mistakes.

## The robustness round

A well-built light channel makes the test "ceiling light on" boring, and that is the right lesson: solving a problem in the hardware instead of the software is a legitimate engineering decision. So the test runs along the axes a tube does not solve.

**Misalignment.** Your setup is slightly turned or shifted sideways before the run. A narrow aperture brings signal but makes you sensitive to misalignment. That trade-off is yours to balance.

**Stray light from the side.** A desk lamp is aimed at the receiver.

**Transport.** The run happens at the test table, not at your desk. Your setup has to be carried and work afterwards.

## Showing it works

At the test table, in front of the other teams. You set up, you get the file, and the run begins.

When it is through, two things happen: the hash is compared, and your receiver opens the file. Everyone then sees on your screen what has just come through the air.

## What you hand in

- The complete protocol specification, as it stands at the final
- All measurement data from the project, in particular on the choice of your symbol rate and alphabet size
- Documentation and a photo of your optical setup
- Your log of mistakes

## Concepts you need

- [Logic and arithmetic](../concepts/logic-and-arithmetic.md)
- [Errors and redundancy](../concepts/errors-and-redundancy.md)
- [Compression](../concepts/compression.md)
- [Throughput and limits](../concepts/throughput-and-limits.md)
- [Encryption](../concepts/encryption.md), for the extra part

## What pays off now

Whoever measured carefully in Challenge 1 has a large alphabet and sends more bits per symbol. Whoever compresses the file before sending has less to transmit. Whoever builds in a checksum notices errors before the whole run is lost.

So this challenge rewards, in hindsight, good work from the weeks before.

## Traps we know about

**Text assumptions in the code.** Whoever has worked with letters so far often has a place somewhere that only works with readable characters. With binary data it shows immediately.

**The starting pattern appears in the data.** With arbitrary bytes this is no longer unlikely. It is to be expected.

**Timed too ambitiously.** A run that gets 90 percent through and then fails at the hash counts for nothing. Safe and slow beats fast and broken.

**The setup does not survive transport.** Tape does not hold what a clamp holds.

## If you finish early

**Encrypt your payload.** Light is public. Any neighbouring team can put its sensor next to yours and read along. Whether your method holds, you can test directly by asking another team to try.
