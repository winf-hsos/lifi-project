"""
Challenge 1: The Alphabet. The receiver.
========================================

This is where you work on the receiving side. The test script calls two
functions in this file, calibrate() and receive_symbol(), and nothing else.

How you build them on the inside is up to you. Add as many functions of your
own as you like.
"""

import time

from lifi_hardware import sensor, use_device

from agreement import ALPHABET_SIZE


# Only when both devices are plugged into the same laptop: remove the # and
# write the UID of the master brick of the RECEIVING device. If you are not
# sure of the UID, run without it first: the error message lists both.
# use_device("put the UID here")


# This is where calibrate() stores what it measured, one reference per symbol.
REFERENCES = {}


# ---------------------------------------------------------------------------
# Calibration
#
# Measure along while the sender plays through its alphabet, and store a
# reference value for each symbol in REFERENCES.
#
# A reference value can be, for example, the average of several readings of
# the same symbol. You decide which of the four sensor values you use for it.
# ---------------------------------------------------------------------------
def calibrate():
    # TODO: measure and fill REFERENCES
    pass


# ---------------------------------------------------------------------------
# Receive one symbol
#
# Measure and return which symbol you think it was, as a number from
# 0 to ALPHABET_SIZE - 1.
#
# You cannot calculate this. Compare the reading with your reference values
# from the calibration and pick the most similar one.
# ---------------------------------------------------------------------------
def receive_symbol():
    # TODO: measure, compare with REFERENCES, return the symbol number
    return 0
