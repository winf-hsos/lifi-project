# Challenge 0, task 4: Measure
#
# You learn: a function that gives something back, and how to take several
#            returned values apart.
#
# Every time you press Enter, the program takes one reading; q and Enter
# stops it. Measure in at least four situations and change only one thing
# between two readings: room light, the sensor covered with your hand, the
# torch of your phone from far away, the torch close up. Write down the
# clear value c for each situation; you need these numbers in task 5.
#
# If a value sticks at 65535, the sensor is overloaded: hold the torch
# further away.
#
# Run it with:  python task_4_measure.py   (on a Mac: python3)

from lifi_hardware import sensor

print("Enter = take a reading, q and Enter = stop")
while True:
    answer = input()
    if answer == "q":
        break
    # TODO: read the sensor, take the result apart into r, g, b, c
    #       and print the four values
    #       Hint: sensor.read() gives back four numbers at once
