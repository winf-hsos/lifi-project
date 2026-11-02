"""
Challenge 1: The Alphabet
=========================

This is where you work. This file contains the contract: five things your team
has to provide. The test script calls these and nothing else.

How you build them on the inside is up to you. Add as many functions of your
own as you like, and feel free to put them in this file.

The rule for the competition: you may use as many symbols as you can reliably
tell apart. A single mistake in 50 runs counts as a fail for that alphabet
size.
"""

import time

from lifi_hardware import led, sensor


# ---------------------------------------------------------------------------
# 1. How big is your alphabet?
#
# In other words: how many different symbols do you use? The symbols are
# numbered from 0 to ALPHABET_SIZE - 1.
#
# Start small. Two symbols to get it running, then go up.
# ---------------------------------------------------------------------------
ALPHABET_SIZE = 2


# ---------------------------------------------------------------------------
# Here you can write down which colour belongs to which symbol.
# The list must have exactly as many entries as ALPHABET_SIZE says.
# ---------------------------------------------------------------------------
SYMBOL_COLORS = [
    (0, 0, 0),          # symbol 0: off
    (255, 255, 255),    # symbol 1: white
    *[
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (0, 255, 255),
        (255, 0, 255),
        (255, 255, 0),
    ][:max(0, ALPHABET_SIZE - 2)],
]


# This is where the receiver stores what it measured during calibration.
REFERENCES = {}


# ---------------------------------------------------------------------------
# 2. Calibration, sender side
#
# Play through your alphabet once so that the other side can learn what your
# symbols look like at its end. Show each symbol several times and long enough.
#
# Important: sender and receiver have to run in the same rhythm here,
# otherwise the receiver assigns its readings to the wrong symbols.
# ---------------------------------------------------------------------------
def calibrate_sender():
    # TODO: show every symbol from 0 to ALPHABET_SIZE - 1 several times
    pass


# ---------------------------------------------------------------------------
# 3. Calibration, receiver side
#
# Measure along while the other side plays through its alphabet, and store a
# reference value for each symbol in REFERENCES.
#
# A reference value can be, for example, the average of several readings of
# the same symbol. You decide which of the four sensor values you use for it.
# ---------------------------------------------------------------------------
def calibrate_receiver():
    # TODO: measure and fill REFERENCES
    pass


# ---------------------------------------------------------------------------
# 4. Send one symbol
#
# index is a number from 0 to ALPHABET_SIZE - 1.
# The function should show the matching symbol and only return once the
# receiver has had enough time to measure.
# ---------------------------------------------------------------------------
def send_symbol(index):
    # TODO: set the matching colour and leave it on long enough
    pass


# ---------------------------------------------------------------------------
# 5. Receive one symbol
#
# Measure and return which symbol you think it was, again as a number from
# 0 to ALPHABET_SIZE - 1.
#
# You cannot calculate this. Compare the reading with your reference values
# from the calibration and pick the most similar one.
# ---------------------------------------------------------------------------
def receive_symbol():
    # TODO: measure, compare with REFERENCES, return the symbol number
    return 0
