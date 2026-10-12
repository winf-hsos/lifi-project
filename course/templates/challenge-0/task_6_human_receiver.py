# Challenge 0, task 6: The human as receiver
#
# You learn: what a receiver actually has to manage.
#
# The program sends a random sequence of colours. One of you watches and
# writes it down without looking at the screen. Afterwards you compare.
#
# Try it several times and change exactly one thing each time:
#   - send faster
#   - use more colours
#   - do not announce when it starts
#   - send the same colour twice in a row
#
# Write down what made it fail each time. This list is exactly the list of
# problems your program has to solve in the coming weeks.
#
# Run it with:  python task_6_human_receiver.py   (on a Mac: python3)

import random
import time

from lifi_hardware import led

colors = {
    "red":   (255, 0, 0),
    "green": (0, 255, 0),
    "blue":  (0, 0, 255),
    "white": (255, 255, 255),
}

names = list(colors.keys())
sequence = [random.choice(names) for _ in range(10)]

input("Receiver ready? Do not look at the screen. Press Enter. ")

for name in sequence:
    led.set_color(*colors[name])
    time.sleep(1.5)          # TODO: make this shorter and see when it breaks
    led.set_color(0, 0, 0)
    time.sleep(0.5)

print()
print("What was sent:")
print("  " + ", ".join(sequence))
print()
print("Compare this with what was written down.")
