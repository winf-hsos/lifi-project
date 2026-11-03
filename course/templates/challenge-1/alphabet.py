"""
Challenge 1: The Alphabet
=========================

How many different colours can you tell apart, without a single mistake?

Everything for this challenge is in this one file. You fill in the
functions below, and run_test at the bottom does the rest. The file works
the same with both devices on one laptop and with one device on each of
two laptops: at the start, the module asks which device sends.

Run it with:  python alphabet.py   (on a Mac: python3)
"""

from lifi_hardware import receiver, run_test, sender

# Your alphabet: one colour per line. Colour number 0 is the first line,
# number 1 the second, and so on. Start with two. When 20 runs get through
# without a mistake, remove the # in front of the next two colours.
COLORS = [
    (0, 0, 0),          # off
    (255, 255, 255),    # white
    # (255, 0, 0),      # red
    # (0, 0, 255),      # blue
    # (0, 255, 0),      # green
    # (255, 255, 0),    # yellow
    # (0, 255, 255),    # cyan
    # (255, 0, 255),    # magenta
]

# What the receiver learns during calibration, one entry per colour
REFERENCES = {}


def calibrate(readings):
    """Called once before the test, after every colour has been shown.

    readings[index] is a list of a few readings, each one Reading(r, g, b, c),
    taken while colour number index was showing.
    """
    for index in readings:
        # TODO: store something better than the first reading, for example
        #       the average of all readings of this colour
        REFERENCES[index] = readings[index][0]


def send_symbol(index):
    """Shows colour number index on the LED of the sending device."""
    r, g, b = COLORS[index]
    sender.led.set_color(r, g, b)


def receive_symbol():
    """Measures and returns the number of the colour it recognised."""
    r, g, b, c = receiver.sensor.read()
    # TODO: compare this reading with REFERENCES and return the number of
    #       the colour that is most similar
    return 0


run_test(send_symbol, receive_symbol, calibrate, symbols=len(COLORS))
