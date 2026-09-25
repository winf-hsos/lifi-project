# Errors and Redundancy

Online: <https://docs.lifi-project.de/concepts/errors-and-redundancy.html>

## Summary

Send enough symbols and one of them will go wrong. That is not bad luck and not bad hardware, it is arithmetic: every single bit has to make it, and the probabilities multiply. So the question is never how to avoid errors but how to notice them, and the tool for that is redundancy, extra bits that carry nothing new and earn their place by what they rule out. A parity bit covers one byte, a checksum covers one frame, a hash covers the whole file, and each of them answers one yes-or-no question and repairs nothing. Noticing is nearly free. Repairing on your own is expensive. Asking for one frame again is almost always the better bargain, and it is why the return channel exists.

In this chapter, we address the following questions:

- Why can transmission errors not be avoided?
- How do you notice that something broke on the way?
- What is a hash, and why does the final compare hashes instead of pictures?
- What does being able to detect errors cost you in sending time?
- Can you repair errors, not just detect them, and what is the price?

You need this concept for [Challenge 4](../challenges/challenge-4.md), where the hash decides whether a run counts at all.

## Explanation

You scan these every day: at the parcel locker, on an e-scooter, on the menu, on the slip with the wifi password. Some of those stickers have been hanging outside for two years. A corner is peeled off, a scratch runs across, dirt and rain did the rest, and the scan still works on the first try. Nobody repaired the sticker, and nobody was asked to hold it up again. Why does that work?

### A code that expects to be damaged

[Figure: A real QR code pointing at docs.lifi-project.de, with 172 of its 1,089 squares cut out of the middle. It still reads.]

The code above points at `docs.lifi-project.de`, and we cut a piece out of its middle: 172 of its 1,089 squares are gone, close to a sixth of the surface. It still reads, and that is measured rather than claimed. A decoder gets the address out of it in the original, blurred, rotated by seven and by twelve degrees, shrunk to 260 pixels, saved as a bad JPEG, and even out of the exported slide image scaled down to 640 pixels wide. Point your phone at it.

The reason is in the way the code is built. It carries 100 bytes. 36 of them carry the data, and that is the 29 characters of the address plus padding. The other 64 carry nothing that is not already there. They exist for the damage. So almost two thirds of this code is dead weight as long as nothing happens, and whoever designed it paid that price in advance, without knowing whether this one sticker would ever be scratched.

That is redundancy, and it is what this chapter is about. A photo that loads halfway and then falls apart into stripes is the other end of the same story: there nobody paid in advance, and at least you can see the damage. The dangerous case is the third one, where you see nothing and a byte is wrong anyway.

### Errors are arithmetic, not bad luck

Take a good link: of a thousand bits one goes wrong, so 99.9 percent arrive correctly. That sounds excellent until you send more than a thousand bits.

[Figure: The chance that everything arrives untouched, at an error rate of 0.1 percent per bit: 92.3 percent for ten characters, 0.03 percent for the same ten characters a hundred times, 0.0000076 percent for the 2 KB payload of the final.]

Ten characters are 80 bits and arrive completely clean with a probability of 92.3 percent. Do the same a hundred times and the probability that all hundred runs were clean is 0.03 percent. Send the 16,384 bits of the final's payload in one go and it drops to 0.0000076 percent. Nothing is broken here. Every single bit has to make it, and the probabilities multiply, so the chance falls off a cliff as the message grows. That is why the question is not how to avoid errors. It is how to notice them.

### The check as a box, twice

[Figure: The check as two boxes: the bytes go into checksum() and a few bits come out; the bytes together with those bits go into check() and the answer is yes or no.]

The model from [Input, Processing, Output](input-processing-output.md) again, as with [compression](compression.md) and [encryption](encryption.md). A fixed rule turns many bytes into a few bits. At the other end the bytes and those bits go into a second box, and what comes out is not the message but an answer: it fits, or it does not. Those extra bits carry nothing that is not already in the data. They are pure redundancy, and that is exactly why errors show up in them.

Note the contrast with compression. There we threw redundancy out to make the file smaller; here we put it back in on purpose. That is not a contradiction. It is a decision about what you spend your bits on.

### One bit that only says: even or odd

You have met the mechanism already: the chain of XOR gates from [Logic and Arithmetic](logic-and-arithmetic.md) that ends in a single check bit. Now it gets a purpose. Sender and receiver agree on even parity, which means the ninth bit is chosen so that the number of ones is even.

[Figure: The byte 1011 0010 has four ones, so the parity bit is 0. After one bit flips there are three ones, an odd number, and the check fails.]

The byte `1011 0010` has four ones, so the parity bit is 0. If one bit flips on the way there are three ones, the count is odd, and the receiver knows this byte is broken. It does not know which bit, only that something is wrong, and that is enough when you can ask again.

But one bit can only say so much:

[Figure: The same byte with two flipped bits: four ones again, the count is even, and the check says nothing.]

With two flipped bits in the same byte the count is even again and parity reports nothing. It catches every odd number of flips and misses every even one. That is not a design flaw, it is the honest price of one extra bit, and it is the general rule for every check there is: a check is never a proof, it is a filter with a known mesh size.

### From one bit to a checksum

Instead of one bit per byte, take one number over the whole frame, computed from every byte by a rule both sides agreed on. The class standard from [Protocols](protocols.md) has the field for it already.

[Figure: The frame with its checksum field, and what more check bits buy: 8 bits let one damaged frame in 256 slip through, 16 bits one in 65,536, 32 bits one in 4,294,967,296.]

A damaged frame now has to hit the expected checksum by chance to get through, and with eight bits that happens about once in 256. With 32 bits it is about once in four billion, which is what PNG and ZIP carry as CRC-32. Two things are worth memorising. A checksum never says where the error was, and it repairs nothing. And more check bits do not catch more errors; they let fewer slip past.

### A fingerprint for a whole file

The third level is one you have probably never looked at, although your computer uses it every time you download something. It is called a hash, and the everyday word for it is a fingerprint.

A fixed rule takes all the bytes of a file and squeezes them into one single number, written here in the hexadecimal notation from [Number Systems](number-systems.md). The interesting part is the length:

[Figure: The letter a, the message meet at noon and the whole raw parrot photo, all three hashed: one byte, twelve bytes and 196,662 bytes, and every result is exactly 64 characters long.]

One letter, a short sentence and a 196,662-byte photo: all three come out as exactly 64 characters. A hash is always the same length, no matter how big the file is. That is the whole point, and it is what makes it useful here: to check whether two files are identical you do not need both files, you only need to compare their fingerprints, and those are 32 bytes instead of two kilobytes. The method in the picture is SHA-256. The name is worth a second: to hash means to chop and mix, as in hashed meat, and that is what happens to the bytes. It is also why you cannot compute backwards from a hash to the file.

Now the property everything depends on:

[Figure: The hash of the raw parrot and the hash of the same parrot with a single flipped bit. Seven of 64 characters still match, which is roughly what two unrelated files would share.]

Above, the fingerprint of the raw parrot photo. Below, the fingerprint of the same photo with a single bit flipped, one bit out of 1,573,296. The two have nothing to do with each other. Seven of the 64 characters happen to match, and that is about what you would expect between any two unrelated files, because with sixteen possible characters per position four matches come for free. There is no similarity, no partial agreement, no slightly-broken. A hash is a test, not a measure: it answers same or not same, and nothing else. If you want to know where the damage sits, you need the per-frame checksums.

[Figure: Three checks and what each one covers: the parity bit one byte, the checksum one frame, the hash the whole file.]

Keep the three apart. The parity bit covers a byte and reports an odd number of flips. The checksum covers a frame and tells you which frame to ask for again, which is what makes targeted retransmission possible. The hash covers the whole file and is what the final compares. And note that a run in which every frame passed its checksum can still fail at the hash, for instance if a frame went missing entirely or arrived twice. That is why you want both.

### One flipped bit, twice

Enough theory. Here is one bit flipped in the middle of the picture data of the raw parrot:

The file opens, the parrot is there, and nobody sees anything. Only the zoom to sixteen by sixteen points shows it: one colour value went from `(240, 45, 38)` to `(240, 45, 166)`, a slightly different red, one value out of 196,608. This is exactly why the final compares a hash and not whether the picture looks good. "It displays" proves nothing at all.

Now the same bit in the same picture, packed as a PNG:

[Figure: The raw file opens with one wrong point; the packed file does not open at all, and its own CRC-32 no longer matches.]

The packed file does not open at all. In a PNG no point stands on its own, because packing works by pointing back at what was written before, which was the whole trick in [compression](compression.md). One wrong bit and the unpacker loses the thread; the viewer only reports that it cannot read the data stream. PNG also notices by itself, because it carries a CRC-32 for every block: stored `a831c3c1`, computed after the flip `cb5ebce6`. The lesson is uncomfortable and matters for the final: the better you pack, the more fragile the transmission becomes. Compression and checking belong together.

### What redundancy costs

Every check is paid for in sending time, so the only real question is how much.

[Figure: Four ways to send 2 KB at 10 bit/s: nothing added takes 27.3 minutes, a checksum per frame 27.7, a parity bit per byte 30.7, every bit three times 81.9.]

The two kilobytes of the final at ten bits per second take 27.3 minutes with nothing added. A 32-bit checksum on every 256-byte frame costs 1.6 percent, half a minute, and in exchange you know of every frame whether it arrived intact. A parity bit per byte costs an eighth of your sending time and still does not catch everything. And sending every bit three times, so that errors can be repaired without asking, costs three times the link: 81.9 minutes instead of 27.3.

### Notice, or repair

Those numbers are the whole decision. You can repair without asking anyone:

[Figure: Every bit sent three times; one of the three flips on the way, and the majority decides. Three times the bits, 82 minutes instead of 27.]

Send every bit three times and let the receiver take the value that occurs at least twice. One flip per triple gets repaired on the spot, without a word back. That is how a space probe does it, because nobody can ask Mars to repeat, and it is the family the torn sticker belongs to as well: a code on a lamppost cannot ask anyone for a second look, so it pays up front, 64 protection bytes against 36 bytes of data. The price is brutal: three times the sending time, always, whether anything breaks or not. And if two bits of the same triple flip, the receiver cheerfully repairs in the wrong direction.

Or you ask:

[Figure: Four frames, the third one fails its checksum, the return channel asks for frame 3 again, and it arrives intact.]

A checksum on every frame, and when one does not fit, that one frame is sent again. While nothing breaks this costs 1.6 percent; when something breaks it costs one frame. Two things belong in your specification for this to work: a frame number, so the sender knows which frame is meant, and a waiting time after which the sender repeats on its own in case the reply itself got lost.

So: whoever can ask back, checks and asks. Whoever cannot ask back has to pay in advance. You can ask back, so build the checksum, not the repetition code, and put the time you save into speed. One more thing for the workshop: check your check. Flip a byte on purpose and see whether your receiver really reports it. A checksum that never fires looks exactly like one that works.

## Slides

The slides for this concept, right here. Page through them with the buttons in the top right corner, or click into the slides and use the arrow keys.

## Practice questions

Try questions in the exam format here, with the answer and its reasoning shown right away.

## Further reading

- Richard W. Hamming: Error Detecting and Error Correcting Codes. Bell System Technical Journal 29 (2), 1950. <https://doi.org/10.1002/j.1538-7305.1950.tb00463.x>. The paper that started error correction, written because Hamming's weekend computer runs kept dying on a single bad bit and nobody was there on Monday to restart them. The first two pages are readable without any mathematics.
- Claude E. Shannon: A Mathematical Theory of Communication. Bell System Technical Journal 27 (3), 1948. <https://doi.org/10.1002/j.1538-7305.1948.tb01338.x>. The same paper that gave us the measure of information also proves the surprising part: on a noisy channel you can get the error rate as close to zero as you like, as long as you send slower than the channel's capacity.
- Ross N. Williams: A Painless Guide to CRC Error Detection Algorithms, 1993. <https://www.zlib.net/crc_v3.txt>. How a real checksum works, written for people who kept finding CRC code they could not understand. Long, informal, and the only text on the subject that reads like a conversation.
- Andrew S. Tanenbaum and David J. Wetherall: Computer Networks. Pearson, 5th edition 2011, chapter 3. The textbook treatment of detection against correction and of the retransmission protocols this page sketches, including what happens when the acknowledgement itself gets lost.
