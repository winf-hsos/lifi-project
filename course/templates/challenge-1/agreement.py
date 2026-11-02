"""
Challenge 1: The Alphabet. What both sides agree on.
=====================================================

The sender and the receiver both read this file. Whatever has to be the same
on both sides belongs here, so that it is written down only once: your
alphabet now, and later perhaps how long a symbol stays on.

Do not use the LED or the sensor in this file. It only holds agreements.
"""


# ---------------------------------------------------------------------------
# Your alphabet: one colour per line
#
# Each line is one symbol. The first line is symbol 0, the next one symbol 1,
# and so on. A colour is three numbers from 0 to 255: red, green, blue.
#
# Start small, with just off and white. For more symbols, remove the # in
# front of the next line, or write a colour of your own.
# ---------------------------------------------------------------------------
SYMBOL_COLORS = [
    (0, 0, 0),          # off
    (255, 255, 255),    # white
    # (255, 0, 0),      # red
    # (0, 255, 0),      # green
    # (0, 0, 255),      # blue
    # (255, 255, 0),    # yellow
    # (0, 255, 255),    # cyan
    # (255, 0, 255),    # magenta
]

# How many symbols you have. This counts the lines above by itself, so you
# never change it by hand.
ALPHABET_SIZE = len(SYMBOL_COLORS)
