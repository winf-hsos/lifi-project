"""
Challenge 0: The Spark
======================

Six small tasks. Each one builds on the one before, and each one teaches you
a basic idea of programming.

Work through the tasks in order. Wherever it says TODO, your code is missing.
You can leave everything else as it is.

You can try out a single task like this:

    python tasks.py 3

And all of them one after the other like this:

    python tasks.py
"""

import sys
import time

from lifi_hardware import led, sensor


# ---------------------------------------------------------------------------
# Task 1: Light on
#
# You learn: calling a function and handing it values.
#
# The LED should shine red for two seconds and then go off.
# ---------------------------------------------------------------------------
def task_1_light_on():
    # TODO: set the LED to red
    #       Hint: led.set_color(red, green, blue), each value from 0 to 255

    time.sleep(2)

    # TODO: switch the LED off again
    pass


# ---------------------------------------------------------------------------
# Task 2: Blink
#
# You learn: a loop, which means doing something several times without
#            writing it several times.
#
# The LED should blink five times: half a second on, half a second off.
# ---------------------------------------------------------------------------
def task_2_blink():
    for i in range(5):
        # TODO: LED on, wait briefly, LED off, wait briefly
        pass


# ---------------------------------------------------------------------------
# Task 3: Colour cycle
#
# You learn: a list, and how to go through it with a loop.
#
# The LED should show all colours from the list one after the other, each for
# one second. Add at least two colours of your own to the list.
# ---------------------------------------------------------------------------
def task_3_color_cycle():
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


# ---------------------------------------------------------------------------
# Task 4: Measure
#
# You learn: a function that gives something back, and how to take several
#            returned values apart.
#
# Measure twenty times and print the values. Hold your hand between the
# devices while it runs and watch how the numbers change.
# ---------------------------------------------------------------------------
def task_4_read_sensor():
    for i in range(20):
        r, g, b, c = sensor.read()
        print(f"Reading {i}:  R={r}  G={g}  B={b}  C={c}")
        time.sleep(0.5)


# ---------------------------------------------------------------------------
# Task 5: React
#
# You learn: a condition, which means doing something different depending on
#            the situation.
#
# The program measures all the time. When it is bright, the LED shines green.
# When it is dark, it shines red. Find the right threshold yourself by looking
# at the numbers from task 4.
#
# This is your first program that makes a decision.
# ---------------------------------------------------------------------------
def task_5_react_to_light():
    threshold = 0   # TODO: enter a sensible value, read off from task 4

    print("Stop with Ctrl+C")
    while True:
        r, g, b, c = sensor.read()

        # TODO: if c is greater than threshold, LED green, otherwise red
        pass

        time.sleep(0.2)


# ---------------------------------------------------------------------------
# Task 6: The human as receiver
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
# ---------------------------------------------------------------------------
def task_6_human_receiver():
    import random

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


# ---------------------------------------------------------------------------
# You do not need to change anything below this line.
# ---------------------------------------------------------------------------
TASKS = {
    1: task_1_light_on,
    2: task_2_blink,
    3: task_3_color_cycle,
    4: task_4_read_sensor,
    5: task_5_react_to_light,
    6: task_6_human_receiver,
}


def main():
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        print(f"--- Task {number} ---")
        TASKS[number]()
        return

    for number, task in TASKS.items():
        print(f"--- Task {number} ---")
        task()
        led.set_color(0, 0, 0)
        time.sleep(1)


if __name__ == "__main__":
    main()
