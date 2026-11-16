"""
Challenge 2: The Word
=====================

How fast can you get three sentences across without a single mistake?

This is your file from Challenge 1, one level up. COLORS, the sensor
settings, calibrate, send_symbol and receive_symbol stay as they were (copy
yours over from alphabet.py). New are the CODEBOOK, which says which colours
stand for which character, SYMBOL_RATE, LENGTH, and four functions you
write. Two of them handle one letter: encode_letter turns a letter into its
colours (encoding), decode_letter turns colours back into a letter
(decoding). The other two handle a whole text by going through it letter by
letter: send_text sends every letter with encode_letter and send_symbol,
receive_text collects colours with receive_symbol and decodes them with
decode_letter. run_test at the bottom hands a sentence to send_text and only
the number of characters to receive_text, and compares what arrives.

From the start on, the timing is yours: run_test starts both functions at
the same moment and then does not help any more.

Run it with:  python word.py   (on a Mac: python3)

For a quick test with your own text and both devices on one laptop, add
text="HELLO WORLD" to the last line; such a run never counts.
"""

import time

from lifi_hardware import receiver, run_test, sender

# Your alphabet from Challenge 1, one colour per line, each with a name
# TODO: copy your own COLORS over from alphabet.py
COLORS = {
    "off":     (0, 0, 0),
    "white":   (255, 255, 255),
    # "red":     (255, 0, 0),
    # "blue":    (0, 0, 255),
}

# The two settings of the receiving sensor, as in Challenge 1
GAIN = 16
INTEGRATION_TIME = 154

# How many colours you send per second. Start slowly and go up step by step.
SYMBOL_RATE = 2

# Which colours stand for which character. Every letter from A to Z and the
# space need an entry. With two colours, five of them make 32 combinations,
# enough for 27 characters. With more colours, fewer per character will do;
# that is the point of Challenge 2.
# TODO: make the CODEBOOK fit your own alphabet: use only the colour names
# from your COLORS, give every character its own sequence, and let more
# colours make the sequences shorter.
CODEBOOK = {
    " ": ["off",   "off",   "off",   "off",   "off"],
    "A": ["off",   "off",   "off",   "off",   "white"],
    "B": ["off",   "off",   "off",   "white", "off"],
    "C": ["off",   "off",   "off",   "white", "white"],
    "D": ["off",   "off",   "white", "off",   "off"],
    "E": ["off",   "off",   "white", "off",   "white"],
    "F": ["off",   "off",   "white", "white", "off"],
    "G": ["off",   "off",   "white", "white", "white"],
    "H": ["off",   "white", "off",   "off",   "off"],
    "I": ["off",   "white", "off",   "off",   "white"],
    "J": ["off",   "white", "off",   "white", "off"],
    "K": ["off",   "white", "off",   "white", "white"],
    "L": ["off",   "white", "white", "off",   "off"],
    "M": ["off",   "white", "white", "off",   "white"],
    "N": ["off",   "white", "white", "white", "off"],
    "O": ["off",   "white", "white", "white", "white"],
    "P": ["white", "off",   "off",   "off",   "off"],
    "Q": ["white", "off",   "off",   "off",   "white"],
    "R": ["white", "off",   "off",   "white", "off"],
    "S": ["white", "off",   "off",   "white", "white"],
    "T": ["white", "off",   "white", "off",   "off"],
    "U": ["white", "off",   "white", "off",   "white"],
    "V": ["white", "off",   "white", "white", "off"],
    "W": ["white", "off",   "white", "white", "white"],
    "X": ["white", "white", "off",   "off",   "off"],
    "Y": ["white", "white", "off",   "off",   "white"],
    "Z": ["white", "white", "off",   "white", "off"],
}

# How many colours one character has in your CODEBOOK
LENGTH = 5

# What the receiver learns during calibration, one entry per colour name
REFERENCES = {}


def calibrate(readings):
    """Your calibrate from Challenge 1: readings[name] is a list of a few
    readings, each one Reading(r, g, b, c), taken while that colour showed."""
    for name in readings:
        # TODO: copy your own version over from alphabet.py
        REFERENCES[name] = readings[name][0]


def send_symbol(name):
    """Shows the colour with this name on the LED of the sending device."""
    r, g, b = COLORS[name]
    sender.led.set_color(r, g, b)


def receive_symbol():
    """Your receive_symbol from Challenge 1: measures and returns the name of
    the colour it recognised."""
    r, g, b, c = receiver.sensor.read()
    # TODO: copy your own version over from alphabet.py
    return "off"


def encode_letter(letter):
    """Encoding: returns the colours of one letter, for example
    ["off", "off", "white", "off", "white"] for "E". Sends nothing."""
    # TODO: look up the colours of letter in CODEBOOK and return them
    return []


def send_text(text):
    """Sends the text letter by letter.

    Encode each letter with encode_letter, then send each of its colours with
    send_symbol and keep it on for 1 / SYMBOL_RATE seconds. As soon as this
    function returns, run_test turns the LED off and stops the clock.
    """
    # TODO: for every letter of text, send the colours from encode_letter
    pass


def decode_letter(colors):
    """Decoding: returns the letter whose colours in CODEBOOK are exactly
    colors, or "?" if there is none."""
    # TODO: find the letter in CODEBOOK whose colours are colors
    return "?"


def receive_text(n_chars):
    """Receives n_chars letters and returns them as one text.

    It starts at the same moment as send_text. The sender shows a new colour
    every 1 / SYMBOL_RATE seconds, so read in the same rhythm: for each
    letter, collect LENGTH colours with receive_symbol, decode them with
    decode_letter and add the letter to the text.
    """
    text = ""
    # TODO: receive n_chars letters and add each one to text
    return text


run_test(send_text, receive_text, calibrate, symbols=COLORS, codebook=CODEBOOK,
         gain=GAIN, integration_time=INTEGRATION_TIME)
