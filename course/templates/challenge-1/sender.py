"""
Challenge 1: The Alphabet. The sender.
======================================

This is where you work on the sending side. The test script calls two
functions in this file, calibrate() and send_symbol(index), and nothing else.

How you build them on the inside is up to you. Add as many functions of your
own as you like.
"""

import time

from lifi_hardware import led, use_device

from agreement import ALPHABET_SIZE, SYMBOL_COLORS


# Only when both devices are plugged into the same laptop: remove the # and
# write the UID of the master brick of the SENDING device. If you are not
# sure of the UID, run without it first: the error message lists both.
# use_device("put the UID here")


# ---------------------------------------------------------------------------
# Calibration
#
# Play through your alphabet once so that the receiver can learn what your
# symbols look like at its end. Show each symbol several times and long enough.
#
# Important: sender and receiver have to run in the same rhythm here,
# otherwise the receiver assigns its readings to the wrong symbols.
# ---------------------------------------------------------------------------
def calibrate():
    # TODO: show every symbol from 0 to ALPHABET_SIZE - 1 several times
    pass


# ---------------------------------------------------------------------------
# Send one symbol
#
# index is a number from 0 to ALPHABET_SIZE - 1.
# The function should show the matching colour and only return once the
# receiver has had enough time to measure.
# ---------------------------------------------------------------------------
def send_symbol(index):
    # TODO: set the matching colour from SYMBOL_COLORS and leave it on long enough
    pass
