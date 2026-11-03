# Challenge 1: The Alphabet

How many different states can you tell apart, without a single mistake, over 20 attempts?

## What you implement

Everything is in one file, `alphabet.py`, no matter whether you work with one laptop or two:

| Part | What goes in |
|---|---|
| `COLORS` | your alphabet, one colour per line; colour number 0 is the first line |
| `calibrate(readings)` | learns what each colour looks like at the receiver, from the readings the test hands over |
| `send_symbol(index)` | shows colour number `index` on the sending LED; this one is already done |
| `receive_symbol()` | measures and returns the number of the colour it recognised |
| `run_test(...)` | the last line; it runs the test and you do not change it |

How you build the functions on the inside is up to you. Add as many functions of your own as you like. `sender.led` is the LED of the sending device, `receiver.sensor` the sensor of the receiving one.

## Why you need a calibration

The receiver cannot calculate which symbol has arrived. Its readings depend on distance, room light and the particular part, and the same colour never gives exactly the same numbers twice.

So it first has to **learn** what your symbols look like in this setup. Before every run, `run_test` shows your whole alphabet once and takes a few readings of each colour. Then it calls your `calibrate(readings)`: `readings[0]` is the list of readings taken while colour 0 was showing, `readings[1]` those of colour 1, and so on. What you keep from them, an average, a range or a rule, is your decision. During the test, `receive_symbol()` compares every new reading with what you kept and picks the most similar colour.

Calibration happens again before every run, at the acceptance test too. After being carried around and under different light, old values would no longer fit.

## Running the test

```bash
python alphabet.py
```

On a Mac use `python3` instead of `python` if needed.

**Both devices on one laptop.** The module finds both, lights up one of them and asks whether that one sends or receives. Then the test runs on its own: show a colour, measure, note, next colour.

**One device on each of two laptops.** Start the same file on both laptops. Each one asks whether it sends or receives. The course server brings the two together through your team and says when the next colour comes, so you do not need to start them at the same moment. Both laptops need WLAN.

Every run gets a fresh random sequence from the course server, so nobody knows it in advance. At the end both sides show the result and every mistake, and the run appears in your [team cockpit](https://lifi.hsos.uber.space/cockpit). Without the server, a run with both devices on one laptop still works as a practice run that does not count.

To practise on purpose even though the server is reachable, switch the server off before you start. With two laptops this does not work, because there the server keeps the two in step.

```bash
# Windows (PowerShell): holds until you close this terminal
$env:LIFI_SERVER="off"
python alphabet.py

# macOS (Terminal): holds for this one call only
LIFI_SERVER=off python3 alphabet.py
```

On Windows, a run you want to count therefore needs a new terminal. On macOS, the next plain `python3 alphabet.py` counts again.

For quick tests in between, fewer runs are enough: change the last line to `run_test(send_symbol, receive_symbol, calibrate, symbols=len(COLORS), runs=5)`. Only runs with 20 attempts count.

## An approach that works

Start with the two colours already in `COLORS`, so just off and white. When that gets through 20 runs without a mistake, go up to 4 by removing the `#` in front of the next two colours, then to 8. At some point mistakes appear, and the last size without mistakes is your result.

It does not pay to gamble high: eight symbols recognised reliably are worth more than sixteen with an occasional mix-up.

When there are mistakes, the result tells you what they look like. If the same two colours are mixed up every time, they are too close together. If it looks random, the calibration is the more likely culprit.

## What to keep

Optional and only for your team: nobody grades it, and the bonus depends only on passing the challenges. Worth keeping anyway:

- Measurement log without optical aids (the control measurement)
- Measurement log with your setup
- Photo of your setup with a short explanation
- Log of mistakes

## At the acceptance test

You run the test at your own place, with the two boxes of sender and receiver touching wall to wall. Nicolas comes round, looks at your setup and checks your result. There is no live change in Challenge 1: the run with 20 random colours is the whole acceptance, and the largest alphabet that runs without a mistake counts.
