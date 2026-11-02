# Challenge 1: The Alphabet

How many different states can you tell apart, without a single mistake, over 50 attempts?

## What you implement

Everything goes into `device.py`. Five things, and the test script asks for nothing more:

| | What |
|---|---|
| `SYMBOL_COLORS` | your alphabet, one colour per line (`ALPHABET_SIZE` counts them by itself) |
| `calibrate_sender()` | play through your alphabet once |
| `calibrate_receiver()` | measure along and remember reference values |
| `send_symbol(index)` | show one symbol |
| `receive_symbol()` | measure and say which symbol it was |

How you build them on the inside is up to you. Add as many functions of your own as you like.

## Why you need a calibration

The receiver cannot calculate which symbol has arrived. Its readings depend on distance, room light and the particular part, and the same colour never gives exactly the same numbers twice.

So it first has to **learn** what your symbols look like in this setup. That is exactly what calibration is: the sender plays through its alphabet, the receiver measures along and stores a reference value for each symbol. During the run it then compares every new reading with these references and picks the most similar one.

Two consequences of this are easy to overlook. First, both sides have to run in the same rhythm during calibration, otherwise the receiver assigns its readings to the wrong symbols. Second, calibration has to happen again **before every run**, at the test table too. After being carried around and under different light, the old values no longer fit.

## Testing

On both computers, each in its own role:

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
