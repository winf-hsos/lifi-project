<!-- Lecture notes for the slides on `symbols-and-information`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/symbols-and-information.html -->

# Lecture notes: what light means (Symbols and Information)

This text explains the input on the concept "Symbols and Information" for you to read afterwards. It follows the order of the slides, and the references count frames (every build-up step is a frame of its own), but you can also read it without the slides.

The deck is the second of two inputs in the same session; the first, [drawing the line](../analog-and-digital/skript.md), clarifies what digital means in the first place and where the boundaries between the states lie.

## What makes light mean something? (Frame 4)

North Atlantic, 1942. Radio silence, because radio traffic draws the enemy. Two ships talk to each other anyway: a lamp, a shutter in front of it, short short short long.

The light itself knows nothing. It means something only because both sides carry the same table in their heads.

## A symbol is an agreed, distinguishable state (Frames 5 to 7)

Both words carry weight.

**Distinguishable** is a question for physics and for your sensor: can the receiver tell this state apart from all the others? That was the subject of the first input in this session.

**Agreed** is a question for the two of you: did sender and receiver give the same state the same meaning, and did they do it beforehand? No measurement can answer this question.

## Perfect reception, perfect nonsense (Frames 8 and 9)

Two volunteers secretly get different mapping tables. The sender sends four colours, all four arrive without error, and the receiver reads a completely different word.

No transmission error, no interference, no bad measurement. The message is worthless all the same, because the agreement was missing. That is exactly why "agreed" stands in the definition on equal footing with "distinguishable".

## The agreement, written down (Frame 10)

In code, the agreement is a dictionary:

```python
ALPHABET = {
    "red":    "00",
    "green":  "01",
    "blue":   "10",
    "yellow": "11",
}
```

This table is never transmitted. It has to sit on both sides beforehand, which makes it not data but a promise. Whoever changes it without telling the partner rebuilds the nonsense slide.

## The guessing game, measured (Frames 12 to 14)

One of 32 cards has been drawn, and only yes/no questions are allowed. Whoever always halves is done after five questions: 32, 16, 8, 4, 2, 1.

Five, and in every case, not just when you are lucky. This number of necessary halvings is the measure this part is about.

## Not every answer is worth one bit (Frame 15)

The counter-check. "Is it the ace of spades?" can settle everything at once, but it does so in only one of 32 cases. In the other 31, almost everything is still left.

The halving question, on the other hand, always delivers the same result: exactly one halving, whatever the answer. **You cannot choose which answer you get**, and that is why what counts is not the best case but the average.

## What a question is worth on average (Frame 16)

| question | answer | chance | you learn | on average |
| --- | --- | --- | --- | --- |
| "is it red?" | yes | 1/2 | 1 bit | 1 bit |
| | no | 1/2 | 1 bit | |
| "is it the ace of spades?" | yes | 1/32 | 5 bit | 0.2 bit |
| | no | 31/32 | 0.05 bit | |

A rare answer carries a lot, an expected one little. But because the rare answer is rare, on average the question whose outcome is open wins. The lopsided question only pays off right at the end, when just two possibilities are left.

## And in general (Frames 17 and 18)

The same calculation, only without the concrete numbers. Every possible answer contributes two things: how likely it is, and what it would be worth. Multiply the two and add them up over all answers, and you get the **expected value** of a question:

`E = Σ pᵢ · log₂(1/pᵢ)`

Here `pᵢ` is the probability of an answer and `log₂(1/pᵢ)` is what that answer would be worth: the less likely it is, the more it carries. For a yes/no question that is exactly two terms, for a question with more outcomes correspondingly more.

Put the numbers in and you get the two rows from before: `0.5 · 1 + 0.5 · 1 = 1` bit for the halving question, `0.03 · 5 + 0.97 · 0.05 = 0.2` bits for the lopsided one. **A whole bit goes only to whoever really halves**, and that holds regardless of how the game turns out this time.

## One bit, and two formulas (Frames 19 and 20)

A **bit** is the amount of information in a decision between two equally likely possibilities. A light switch holds one, and no computer is required for it.

With that, both quantities can be written down, in this order:

**Uncertainty:** `H = log₂(N)` for N equally likely possibilities. It measures how many halvings are still missing.

**Information:** `I = H₁ − H₂`, uncertainty before minus uncertainty after. It measures what an answer has actually removed.

The 32 cards are **not** the uncertainty, they are the space of possibilities. The uncertainty is the 5 bits. A halving question lowers H by exactly 1, so its answer is worth 1 bit.

## Try it yourself (Frame 21)

In [The Question Game](https://winf-hsos.github.io/lifi-concept-demos/question-game/) you are looking for one of sixteen faces. After every question the demo works out what it was worth, and beforehand it shows what the question brings in expected value.

Two rounds are worth playing: once guessing on purpose, once halving. Afterwards the difference is on the screen in bits.

## What a bigger alphabet buys (Frames 22 to 24)

The same tool, now applied to your alphabet. A symbol from N equally likely possibilities carries `log₂(N)` bits: two colours one bit, four colours two, eight colours three, sixteen colours four.

Because the same file then needs fewer symbols, it gets through sooner. At the same symbol rate, with eight colours it needs only a third of the time it needed with two colours.

## Two symbols are enough for anything (Frame 25)

What a large alphabet does per symbol, two symbols do in a group. Five flashes with two possibilities each make `2⁵ = 32` combinations, enough for a whole alphabet.

That is exactly why every computer gets by with nought and one, and exactly why a small alphabet is not a dead end but merely slower.

## When symbols are not equally likely (Frame 26)

So far all symbols counted as equally likely. In real text they are not, and Morse code exploits that: the most common letter, the "e", gets the shortest code, a single dot. Rare letters like the "q" are long.

That pays off because it makes the average message shorter. Every compression scheme rests on this observation, and we will come back to it.

## The catch (Frame 28)

On the left, the gain: more bits per symbol, the same file with fewer symbols, done sooner. On the right, the price: the colours move closer together, the noise reaches across the gap, and symbols are misread.

No formula tells you where the limit is. The size of your alphabet is not a matter of taste, it is a measurement. The other half of this is on [Signal and Noise](../../website/concepts/signal-and-noise.qmd).

## In the workshop (Frame 29)

Four steps, and the first is the one everyone wants to skip:

1. agree on your alphabet **and write it down**
2. measure a profile for every symbol
3. fill `send_symbol()` and `receive_symbol()`
4. run a whole word and count the errors

## To close (Frames 30 and 31)

Light means nothing until you agree what it means. And how much it means, you can count.
