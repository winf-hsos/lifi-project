# Challenge 2: The Word

How fast can you get three sentences across without a single mistake?

## What you implement

Everything is in one file, `word.py`, as in Challenge 1. It is your `alphabet.py` one level up:

| Part | What goes in |
|---|---|
| `COLORS`, `GAIN`, `INTEGRATION_TIME` | your alphabet and the sensor settings, copied over from `alphabet.py` |
| `calibrate(readings)`, `send_symbol(name)`, `receive_symbol()` | your functions from Challenge 1, copied over |
| `SYMBOL_RATE` | how many colours you send per second |
| `CODEBOOK`, `LENGTH` | which colours stand for which character (every letter from A to Z and the space), and how many colours one character has |
| `encode_letter(letter)` | the encoding of one letter: returns its colours from `CODEBOOK` and sends nothing; yours to write |
| `send_text(text)` | goes through the text letter by letter, encodes each one with `encode_letter` and shows its colours with `send_symbol`, one every `1 / SYMBOL_RATE` seconds; yours to write |
| `decode_letter(colors)` | the decoding of one letter: returns the letter whose colours are exactly `colors`, or `"?"`; yours to write |
| `receive_text(n_chars)` | reads the colours in the same rhythm with `receive_symbol`, decodes every `LENGTH` of them with `decode_letter` and returns the letters as one text; yours to write |
| `run_test(...)` | the last line; it runs the test and you do not change it |

The contract has moved up one level. The test hands you text and expects text back. Your functions `send_symbol` and `receive_symbol` are now your own tools inside `send_text` and `receive_text` and are no longer called from outside. That is exactly what an abstraction layer is: from above you see text, from inside you see colours. In between sits the codebook, and two small functions translate with it: `encode_letter` from letter to colours, `decode_letter` from colours back to letter. That way the loop over a long text stays apart from the question of how one single letter is coded, and you can test each letter function on its own, without any device: `print(encode_letter("E"))` and `print(decode_letter(encode_letter("E")))` have to give back what you expect.

## What is new

**The codebook.** The template starts with two colours, off and white, and gives every character five of them: five places with two possibilities make 32 combinations, enough for 26 letters and the space. With four colours, three places would do (64 combinations), with eight colours two (64 again). Fewer colours per character means a shorter sentence on the wire. Whether your receiver still tells them apart at that speed is what you find out by measuring.

**The rhythm.** From the start on, nothing keeps sender and receiver in step except your own code. The sender shows a new colour every `1 / SYMBOL_RATE` seconds; the receiver has to read in the same rhythm. When it reads too early or too late, it sees a colour twice or misses one. Where in each time slot you read, and how long one reading takes at your integration time, decides how fast you can go.

## Running the test

```bash
python word.py
```

On a Mac use `python3` instead of `python` if needed. As in Challenge 1, the same file works with both devices on one laptop and with one device on each of two laptops; at the start, the module asks which device sends.

A run has four parts. First the calibration: `run_test` shows every colour of `COLORS` once and calls your `calibrate`. Then three sentences, each three real words in capital letters with a space between them, such as `BUSY FROGS DANCE`, fresh from the course server for every run. For each one, `run_test` starts `send_text` on the sending device and `receive_text` on the receiving one at the same moment. The receiver only learns how many characters are coming, never the sentence. When `send_text` returns, the LED goes off.

With two laptops, the course server gives both the moment of the start, and each laptop turns it into its own clock. The two starts agree to within a few hundredths of a second, not exactly; at high rates your receiver will notice. Both laptops need WLAN. Without the server, a run with both devices on one laptop still works as a practice run that does not count.

At the end both sides show each sentence as sent and as received, with every wrong character in red, and the speed of the run. The run appears in your [team cockpit](https://lifi.hsos.uber.space/cockpit).

For quick tests in between, one sentence is enough: add `sentences=1` to the last line. Only runs with three sentences count. For an even simpler test, send your own text: add `text="HI"` or `text="HELLO WORLD"` to the last line (or a list of texts, sent one after the other). That is a practice run with both devices on one laptop; it does not ask the course server and never counts. Your texts may only hold characters that are in your `CODEBOOK`.

## How the speed is measured

The clock runs from the common start until `send_text` returns. **Characters per second** is the number of characters in the three sentences divided by that time; this is what the ranking on the [challenge board](https://lifi.hsos.uber.space/challenges) goes by. Next to it stands **bit per second**: all colours you sent, divided by the same time, times log2 of the number of colours in `COLORS`. With two colours, one colour carries one bit, with four colours two bits, with eight colours three.

## An approach that works

Start slowly, two colours per second as in the template. When three sentences arrive without a mistake, raise `SYMBOL_RATE` step by step and note where it breaks down. Then try more colours with a shorter codebook. Keep this measurement series; you will need it again in Challenge 3.

Make sure you only ever change **one** thing. Whoever adjusts rate and alphabet size at the same time does not know afterwards which one caused the problem.

When there are mistakes, the result tells you what they look like. Characters missing or appearing twice mean sender and receiver were out of step, which points to timing. Single wrong characters mean colours were mixed up: the rate is too high for your alphabet, or the calibration does not fit.

## What to keep

Optional and only for your team: nobody grades it, and the bonus depends only on passing the challenges. Worth keeping anyway:

- Your codebook: which sequence of colours stands for which character
- Measurement log: at which rates did it work, from which one on did it not?
- Log of mistakes

## At the acceptance test

As in Challenge 1, you run the test at your own place, and Nicolas shows your run live on the projector. **To pass, all three sentences of one run have to arrive without a single mistake**, at any speed; Nicolas then confirms the acceptance. There is no live change. The fastest teams by characters per second show their run in front of everyone at the competition.
