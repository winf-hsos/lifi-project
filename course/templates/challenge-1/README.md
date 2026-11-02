# Challenge 1: The Alphabet

How many different states can you tell apart, without a single mistake, over 50 attempts?

## What you implement

In this challenge one device only sends and the other only receives, so each side has its own file. A third file holds what both sides have to agree on:

| File | What goes in |
|---|---|
| `agreement.py` | `SYMBOL_COLORS`, your alphabet, one colour per line (`ALPHABET_SIZE` counts them by itself) |
| `sender.py` | `calibrate()` plays through your alphabet once, `send_symbol(index)` shows one symbol |
| `receiver.py` | `calibrate()` measures along and remembers reference values, `receive_symbol()` measures and says which symbol it was |

The test script calls these four functions and asks for nothing more. How you build them on the inside is up to you. Add as many functions of your own as you like.

Anything that has to be the same on both sides belongs in `agreement.py`, not twice in the two other files. That way sender and receiver can never disagree about it.

## Why you need a calibration

The receiver cannot calculate which symbol has arrived. Its readings depend on distance, room light and the particular part, and the same colour never gives exactly the same numbers twice.

So it first has to **learn** what your symbols look like in this setup. That is exactly what calibration is: the sender plays through its alphabet, the receiver measures along and stores a reference value for each symbol. During the run it then compares every new reading with these references and picks the most similar one.

Two consequences of this are easy to overlook. First, both sides have to run in the same rhythm during calibration, otherwise the receiver assigns its readings to the wrong symbols. Second, calibration has to happen again **before every run**, at the test table too. After being carried around and under different light, the old values no longer fit.

## Testing

Start the test twice, each in its own role:

```bash
python run_test.py sender
python run_test.py receiver
```

Both sides write a log, `sent.txt` and `received.txt`. Put both files into one folder and compare them:

```bash
python compare.py
```

For quick tests in between, fewer runs are enough:

```bash
python run_test.py sender --runs 10
```

This script is exactly what runs at the acceptance test. So you can rehearse the scored run as often as you like beforehand.

## Both devices on one laptop

You can also plug both devices of your team into the same laptop and start sender and receiver in two terminals next to each other. Then both logs end up in the same folder, and `compare.py` runs straight away.

The module then has to know which device is which. At the top of `sender.py` and `receiver.py` there is a line `# use_device("put the UID here")`. Remove the `#` in both files and write in the UID of the master brick of that device: the sending one in `sender.py`, the receiving one in `receiver.py`. If you do not know the UIDs, start without them first; the error message lists both, and the Brick Viewer shows which one belongs to which box. With only one device plugged in, leave the line as it is.

One thing gets harder: you cannot press Enter in both terminals at the same moment. Between the first and the second there is easily a second. Your calibration has to cope with that.

## An approach that works

Start with the two colours already in `SYMBOL_COLORS`, so just off and white. When that gets through 50 runs without a mistake, go up to 4 by removing the `#` in front of the next two colours, then to 8. At some point mistakes appear, and the last size without mistakes is your result.

It does not pay to gamble high: eight symbols recognised reliably are worth more than sixteen with an occasional mix-up.

When there are mistakes, `compare.py` also tells you what they look like. If the same two symbols are mixed up every time, they are too close together. If it looks random, the timing or the calibration is the more likely culprit.

## What to keep

Optional and only for your team: nobody grades it, and the bonus depends only on passing the challenges. Worth keeping anyway:

- Measurement log without optical aids (the control measurement)
- Measurement log with your setup
- Photo of your setup with a short explanation
- Log of mistakes

## At the acceptance test

You set up at the test table, calibrate, and the run starts. After that comes a live change, for example: "Go up to twelve symbols and run it again." For that you have to find the places in your code that depend on the alphabet size.
