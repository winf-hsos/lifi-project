# Protocols

Online: <https://docs.lifi-project.de/concepts/protocols.html>

## Summary

A protocol lays down, completely, how two sides exchange messages. Not only what the symbols mean, but where a message starts, where it ends, in what order things arrive, and what happens when something goes wrong. None of that comes out of the sensor. All of it is something you agree on, and every part of the agreement has a price tag. The test of a protocol is not whether it works between the two of you. The test is whether somebody who has never spoken to you can build a receiver from your description.

In this chapter, we address the following questions:

- What has to be settled before two sides can talk to each other at all?
- How does a receiver recognise the start and the end of a message?
- Why does a start pattern have to be longer than a single symbol?
- Why does a receiver need a memory, and what happens without one?
- When is a description complete enough for somebody else to implement it?

You need this concept for [Challenge 2](../challenges/challenge-2.md) and above all for [Challenge 3](../challenges/challenge-3.md). The neighbouring question, how two devices stay in step without a shared clock, belongs to [Sampling and Synchronization](sampling-and-synchronization.md); here it is about the agreement on what gets sent.

## Explanation

A distress call on marine radio always begins with "mayday" three times. Not out of tidiness: the channel is noisy, and nobody knows when a call begins. A single word gets lost or could be chance; three identical words in a row are a pattern that noise does not produce. After that the call has a fixed shape: who is calling whom, then the message, then "over" (I am done, your turn) or "out" (conversation finished). Sailors worked this out a century ago, and it is exactly what your receiver needs from Challenge 3 onwards.

### So far, a human said "now"

In Challenges 1 and 2 somebody started both programs one after the other, pressing enter on two machines. That made the start unambiguous, and the receiver knew the length of the message as well. Both of those helpers now disappear. The receiver runs before the sender starts, and it sees readings all the time, because the room is never dark.

[Figure: What a running receiver actually sees: the room on the left and on the right, the message somewhere in the middle. Nothing about the numbers themselves says where it begins or where it stops.]

That is the sentence this chapter turns on: a bit stream without a frame means nothing. Bits become a message once both sides know where it starts, where it ends and what it means. No sensor delivers that frame. You agree on it.

Three questions have to be answered by your agreement. Where does it start? Where does it end? And what does the receiver do when something goes wrong, for instance when an expected pattern never arrives? The third one is the one everybody forgets, because in the normal case it never shows.

### The start: the preamble

If somebody at the front of the room sends a few random colours, then a message, then random colours again, nobody finds the start. If instead every message begins with the same conspicuous sequence, say red-blue three times, the room spots the start by itself after two rounds. That sequence is called a **preamble**: an agreed pattern in front of the message that carries no information and says only "from here on". It replaces the human who used to press enter.

[Figure: The same stream, now with the agreed pattern in front of the message. The preamble carries nothing; its whole job is to be recognisable.]

Two properties make a preamble usable: it is agreed, and it does not occur in noise. Two things follow from that. First, it is built from active colours, not from light and dark: an LED that is off looks to the sensor exactly like the room, so a pattern with an off-part would be half noise. Second, a single symbol is not enough.

[Figure: The same noise twice. On top a single red is the start pattern, and the room produces it by itself again and again: three false starts are marked. Underneath, the pattern is red, blue, red, blue, red, blue, and chance essentially never builds it.]

The longer and the more regular the pattern, the more rarely chance imitates it. If you are fighting false starts, change the agreement, not the gain or the integration time: those lift the noise exactly as much as the signal.

### What the frame costs

The run-up is not free, and it is worth working the number out rather than waving at it.

[Figure: The same frame around two messages. Nine symbols carry no payload in both cases; what changes is how much message they sit in front of.]

Six symbols of preamble plus three symbols of end marker are nine symbols that carry nothing. Five characters at eight bits each are 40 symbols of data with two colours, so you send 49 and nine of them are frame: about 18 %. The same nine symbols in front of a 20-character message are nine out of 169, about 5 %. The frame costs the same per message no matter how long the message is, which means short messages pay for it most. For Challenge 4 that argues for few long messages rather than many short ones.

### When the data looks like the start

One question your specification has to answer: what happens if the preamble turns up by chance in the middle of a message?

[Figure: The agreed pattern appears a second time, this time inside the data. A receiver that keeps scanning for it treats that as a new start, throws away what it had, and begins again in the middle.]

The problem is real and has a name in practice. There is more than one good answer, and your specification has to pick one. Making the preamble longer is *not* one of them: that lowers the probability without removing it. What does work: only scan for the pattern while you are waiting, and ignore it while reading; or send a length field so the receiver counts instead of scanning; or reserve a colour and drop it from the data alphabet, so the sequence cannot occur in the data at all. The last one costs capacity, because your alphabet gets smaller.

### The end: length field or end marker

If the sender transmits two messages back to back, the receiver has to know where the first one stops. There are two answers, and both are right.

[Figure: A length field at the start against an end marker after the last character, each with what it buys and what it costs.]

A **length field** stands at the start and says how many characters follow; the receiver counts along. Its price: the field has to arrive intact, or it ruins the whole message, and its size limits the message, with 8 bits to 255 characters. An **end marker** is an agreed symbol after the last character; the receiver stops as soon as it arrives, and the message may be any length. Its price is the same question as with the preamble: the marker must not occur by chance in the data. The clean way around that is a **reserved symbol**, a colour that does not appear in your data alphabet at all.

What does not work is relying on the next preamble to mark the end of the previous message, because then the last message never ends. And the receiver cannot tell from the content that a word is "complete", because it does not know the content. The end has to follow from the agreement, not from the text.

### A program with a memory

Your receiver has just recognised a red. What should it do with it? That cannot be decided from the reading alone. While it is waiting for the start, the red is either noise or part of the preamble; while it is reading a message, it is a data symbol. Same reading, different reactions, depending on what came before. So the receiver needs a memory: a **state** that records where it is.

[Figure: The two states of the receiver, reading the same stream symbol by symbol. While waiting, everything that is not the pattern is discarded; while reading, everything is kept until the end marker arrives.]

In Python a state is only a variable, say `state`, with one branch per state inside the loop. In `waiting`, the only check is whether the start pattern is complete; in `reading`, every symbol is appended until the end marker arrives, and then the message is handed over and the state is reset. That arrow back matters more than it looks: forget the reset and you have a receiver that can read exactly one message. It is the most common fault at the acceptance test, and the live change "two messages back to back" finds it immediately. The program does not crash, either; an unhandled state simply does nothing in Python, and the second message disappears without a sound.

### When the end never comes

Now the third of the three questions. Halfway through a message somebody puts a hand into the beam, the rest never arrives, and the end marker never comes.

[Figure: The transmission breaks off. The receiver stays in the reading state, and the next message begins with its preamble in vain: it is not looking for one any more.]

The obvious thought is that this message is lost, which is bad luck. That is not what happens. The receiver is stuck in `reading` and no longer scans for the preamble at all, because it only does that while waiting. It does not lose this message; it loses every message from now on. So the specification needs an abort rule: if the end marker has not arrived after an agreed time or number of symbols, discard what you have and go back to waiting. And if you do output fragments, label them: half a message passing as a whole one is worse than none at all.

### The agreement somebody else can implement

Nothing about a protocol is self-evident, and all of it has to be settled before the first bit: the symbols, the start, the end, the timing, the failure case. The test is not whether it works between the two of you. The test is whether somebody who does not know you can build a receiver from it. That is exactly what happens at the interop test in Challenge 3.

[Figure: A specification that looks complete. Two lines are missing, and a team that has never spoken to you will fall over both of them.]

The test reads: cross out everything you know but did not write down. Is the rest enough? The classic gap is time. Symbols, preamble, character code and end marker are all there, but not how long a symbol stands. To you that is obvious; to another team the specification is unbuildable, because without the symbol duration they cannot even sample the start pattern reliably. The second gap is the failure case. A complete example, say `HI` written out as the full sequence of symbols including start and end, saves more specifications than any amount of prose. And if the other team's receiver does not understand your messages while everything works between your own devices, that is first of all a finding about your document, not about the other team.

At the end of Challenge 3 the class agrees on one common frame, built from your proposals. That is how standards really come about: not on a drawing board, but from comparing solutions that work. A standard is an agreement between people, not a technical necessity. What lies below the frame, the colours, the speed, the calibration, stays yours afterwards.

## Slides

The slides for this concept, right here. Page through them with the buttons in the top right corner, or click into the slides and use the arrow keys. The other buttons give you full screen, the slides in a new tab, and the deck as a PDF.

## Practice questions

Try questions in the exam format here, with the answer and its reasoning shown right away.

## Further reading

- Charles Petzold: Code. The Hidden Language of Computer Hardware and Software. Microsoft Press, 2nd edition 2022. Chapter 20 builds a message out of an agreement and shows how much of a "code" is convention rather than technology.
- Marc Levinson: The Box. How the Shipping Container Made the World Smaller and the World Economy Bigger. Princeton University Press, 2nd edition 2016. The story of a standard that changed the world, and of the decades of arguing it took to agree on a set of dimensions that nobody thought were the best ones.
- RFC 793, Transmission Control Protocol, 1981. <https://www.rfc-editor.org/rfc/rfc793>. The document that runs most of the internet. You are not meant to read it through; look at section 3.1, the header diagram, and find the fields you have just invented yourselves.
