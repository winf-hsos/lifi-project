# Challenge 0, task 3: Colour cycle
#
# You learn: a list, and how to go through it with a loop.
#
# The LED should show all colours from the list one after the other, each for
# one second. Add at least two colours of your own to the list.
#
# Run it with:  python task_3_color_cycle.py   (on a Mac: python3)

import time

from lifi_hardware import led

colors = [
    (255, 0, 0),      # red
    (0, 255, 0),      # green
    (0, 0, 255),      # blue
    # TODO: add at least two colours of your own
]

for color in colors:
    # TODO: set this colour and wait one second
    #       Hint: the three numbers are together in color
    pass
