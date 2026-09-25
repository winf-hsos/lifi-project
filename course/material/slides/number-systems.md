<!-- Lecture notes for the slides on `number-systems`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/number-systems.html -->

# Lecture notes: why ten? (Number Systems)

This text explains the input on the concept "Number Systems" for reading afterwards. It follows the order of the slides, and the references count frames (every build-up step is a frame of its own), but it can also be read without the slides.

The deck is the first of two inputs in the same session; the second, [Code Systems](../code-systems/skript.md), answers the question of what the numbers that come about here mean.

One scheme carries the whole input: the digits at the top, the place values below them, the sum at the bottom. It comes three times, with base 10, base 8 and base 2, and after that twice more, with base 16 and with your colours. Once you have seen it, you can read any base without learning a new rule.

## Why do we count to ten? (Frame 4)

Ask around why our number system has ten digits, of all numbers. The answers usually come out reverent: because it divides nicely, because it is mathematically practical, because that is how it grew.

The right answer is more banal. We have ten fingers. That is all. There is no constant of nature in it and no special property of ten, only anatomy.

That is the hook for everything that follows. If the ten is a coincidence, then it can be done differently, and everything that seems self-evident about the way we write numbers falls into two parts: one that is pure convention, and another that is mathematics and works the same way in every system.

## What 123 really says (Frames 5 and 6)

Take the number 123. What does it actually say?

Not "one, two, three". It says: one hundred, two tens, three ones. Every place carries a power of ten, and the digit only says how often that power occurs.

    1 · 100  +  2 · 10  +  3 · 1  =  123

Everybody knows that, but hardly anyone has ever written it down like this. Exactly this recipe is called a **place value system**, and it is the only reason ten digits are enough for infinitely many numbers: instead of inventing a new symbol for every number, you give the position a meaning.

## The eight-finger creature writes 123 (Frames 7 and 8)

Now picture a creature with eight fingers. It invented the same procedure, but it counts to eight before the place overflows. It also writes `123` on a sheet of paper.

Which number does it mean? Work it out before you read on.

The same scheme, only powers of eight instead of powers of ten: 64, 8, 1.

    1 · 64  +  2 · 8  +  3 · 1  =  83

The same three digits, the same procedure, a different number. From this follows something that carries the rest of the session: a string of digits on its own means nothing at all, as long as the base is not written next to it.

## Two flippers: counting in binary (Frames 9 and 10)

The dolphin in Frame 9 has two flippers. So its number system knows exactly two digits, 0 and 1, and that is the trick in the setup.

| us | the dolphin |
| --- | ---------- |
| 0 | 0 |
| 1 | 1 |
| 2 | 10 |
| 3 | 11 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |
| 8 | 1000 |

Count along together. At the step from 1 to 10 most people hesitate for a moment, and then the penny drops: this is exactly the same thing that happens for us between 9 and 10. The digits are used up, so a new place is opened. It is just that with two digits it happens all the time, and the numbers get long quickly.

## The dolphin writes 110 (Frames 11 and 12)

The scheme for the third time, and now it sticks. Powers of two: 4, 2, 1.

    1 · 4  +  1 · 2  +  0 · 1  =  6

`110` is not one hundred and ten. If you have come along this far, you can read any base, because there is no new rule any more. It is always the same: digit times place value, added up.

## Why two, of all things? (Frames 14 and 15)

A computer could in principle use any base. Decimal computers really did exist, and they died out. Why?

The answer is not mathematics but engineering. Imagine a wire carrying a voltage between zero and five volts. If you want to send ten digits, you have to cut this range into ten compartments, and each compartment is half a volt wide. If you want to send two digits, there are two compartments of two and a half volts.

Now every real wire wobbles. Cables act as antennas, components warm up, power supplies hum. The same wobble that never matters with two compartments regularly throws the digit into the neighbouring compartment with ten. This is the measurement slide from "Analog and Digital", read from the other side: the more states have to fit into the same range, the smaller the gaps, and the sooner noise wins.

Two states are the cheapest thing you can build reliably. On and off, current and no current, bright and dark. The price for that is more places, and places are cheap.

## Eight bits make a byte (Frames 16 to 18)

The same scheme with eight places. The place values are 128, 64, 32, 16, 8, 4, 2, 1, each place double its right-hand neighbour.

    0 1 0 0 0 0 0 1   →   64 + 1 = 65

Eight places with two possibilities each give 2⁸ equals 256 values, read as a number 0 to 255. That is why the colour channels of your LED run from 0 to 255: one channel is exactly one byte.

You know the word **bit** from session 4 as a measure of information, and here it turns up again as a digit, as binary digit. That is no coincidence and no pun: a place with two possible values holds exactly one yes/no answer. The container is named after its content. The distinction is still useful, though, because a container can also be half empty; compression comes back to that.

To try it yourself there is the [Byte Switchboard](https://winf-hsos.github.io/lifi-concept-demos/byte-switchboard/): eight switches, and the number follows along. Three questions are worth asking there: Which switch changes the most? How do you set 255, and how 1? And what happens if you want to count one further from 255?

## Hexadecimal: four bits at a time (Frames 20 to 23)

Nobody can read eight zeroes and ones at a glance. There is a shorthand for that, and it is not a new number system in the proper sense, but the same scheme with base 16.

The reason for sixteen, of all numbers, lies in the byte. Four bits have 2⁴ equals 16 states, and 16 is exactly the number of hex digits. So one hex digit fits a packet of four, and a whole byte fits into two digits:

    1101 0010   →   D2

Because our ten digits are not enough for sixteen values, six letters are borrowed: A stands for 10, B for 11, and so on up to F for 15. Once you have seen this table, you can read any hex dump.

Exactly such a dump is in the demonstrator [Inside a File](https://winf-hsos.github.io/lifi-concept-demos/inside-a-file/): on the left the bytes of a real file in hexadecimal, on the right the same bytes as characters. Two things can be seen there. First, the very first bytes give away what kind of file it is. Second, between the readable positions there are just as many unreadable ones, and both are the same stuff. A file is nothing but a sequence of numbers.

And with that the colour notation `#AC8909` also becomes something you can work out: three bytes, two hex digits each, one byte per colour channel.

## Two ladders of units (Frame 24)

Before the famous hard disk puzzle comes, two ladders side by side.

The decimal ladder takes a factor of 1000 per rung: kilobyte, megabyte, gigabyte, terabyte. The binary ladder takes 1024, because storage is organised in powers of two and 2¹⁰ equals 1024 is the round binary number closest to 1000.

| Step | decimal | binary |
| ----- | ------- | ----- |
| Byte | 1 | 1 |
| Kilo | 1 000 | 1 024 |
| Mega | 1 000 000 | 1 048 576 |
| Giga | 1 000 000 000 | 1 073 741 824 |
| Tera | 1 000 000 000 000 | 1 099 511 627 776 |

In everyday speech both ladders have the same names. If you want to be precise, you say kibibyte, mebibyte, gibibyte for the binary rung, but almost nobody does, and that is where the puzzle on the next slide comes from.

## The missing 69 gigabytes (Frames 25 and 26)

The box says 1 terabyte. You install the disk, and the computer shows 931 gigabytes. Who is cheating here?

Guess first, before you read on.

Nobody is cheating. The manufacturer counts up the decimal ladder, and for them a terabyte is a trillion bytes. The operating system takes exactly the same trillion bytes and divides it down the binary ladder, by 1024³, and arrives at 931. Not a single byte is missing. Over four rungs the difference adds up to roughly seven percent, and both sides call their rung a gigabyte.

That is not fraud, it is a word problem.

## You built one long ago (Frames 28 to 30)

And now for the punchline. Your colour alphabet is a place value system, and the number of your colours is the base.

If you can reliably tell four colours apart, you are working in base 4. Decide which colour is which digit, say red for 0, green for 1, blue for 2, yellow for 3. Then the colour sequence red-yellow-green is the number

    0 · 16  +  3 · 4  +  1 · 1  =  13

and with three places 4³ equals 64 combinations are available, enough for an alphabet of 26 letters.

Two things follow from this for Challenge 1. First, the order is part of the message: red-yellow-green and green-yellow-red are different code words, for exactly the same reason that 123 and 321 are different numbers. Second, the arithmetic works in both directions. If you know how many characters you have to distinguish, you can work out how many places you need for that, and if you decide on a number of colours, you know at once how long your code words will be.

## Ten was never special (Frames 31 and 32)

The closing sentence is the opening sentence seen from the other side. Ten is the number of fingers on two hands, and nothing else.

Once you have seen that, you will no longer think of any base as natural, or of any as difficult. Binary, hexadecimal and your colour system are the same procedure with different digits.
