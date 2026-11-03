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

# Your alphabet: one colour per line, each with a name. The names are what
# your functions work with and what the result shows. Start with two. When
# 20 runs get through without a mistake, remove the # in front of the next
# two colours.
COLORS = {
    "off":     (0, 0, 0),
    "white":   (255, 255, 255),
    # "red":     (255, 0, 0),
    # "blue":    (0, 0, 255),
    # "green":   (0, 255, 0),
    # "yellow":  (255, 255, 0),
    # "cyan":    (0, 255, 255),
    # "magenta": (255, 0, 255),
}

# What the receiver learns during calibration, one entry per colour name
REFERENCES = {}


def calibrate(readings):
    """Called once before the test, after every colour has been shown.

    readings[name] is a list of a few readings, each one Reading(r, g, b, c),
    taken while the colour with that name was showing, so readings["white"].
    """
    for name in readings:
        # TODO: store something better than the first reading, for example
        #       the average of all readings of this colour
        REFERENCES[name] = readings[name][0]


def send_symbol(name):
    """Shows the colour with this name on the LED of the sending device."""
    r, g, b = COLORS[name]
    sender.led.set_color(r, g, b)


def receive_symbol():
    """Measures and returns the name of the colour it recognised."""
    r, g, b, c = receiver.sensor.read()
    # TODO: compare this reading with REFERENCES and return the name of
    #       the colour that is most similar
    return "off"


run_test(send_symbol, receive_symbol, calibrate, symbols=COLORS)
