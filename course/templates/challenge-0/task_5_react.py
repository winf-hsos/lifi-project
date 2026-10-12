# Challenge 0, task 5: React
#
# You learn: a condition, which means doing something different depending on
#            the situation.
#
# The program measures all the time. When it is bright, the LED shines green.
# When it is dark, it shines red. Find the right threshold yourself: put it
# between the clear value with the sensor covered and the one with the torch
# from your notes of task 4.
#
# This is your first program that makes a decision. It keeps running until
# you stop it with Ctrl+C.
#
# Run it with:  python task_5_react.py   (on a Mac: python3)

import time

from lifi_hardware import led, sensor

threshold = 0   # TODO: a value between "covered" and "torch" from task 4

print("Stop with Ctrl+C")
while True:
    r, g, b, c = sensor.read()

    # TODO: if c is greater than threshold, LED green, otherwise red

    time.sleep(0.2)
