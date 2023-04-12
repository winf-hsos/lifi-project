import constants

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

# Create IP-connection
ipcon = IPConnection()
ipcon.connect(constants.HOST, constants.PORT)

# Create OLED object
oled = BrickletOLED128x64V2(constants.UID_OLED_DISPLAY, ipcon)

# Clear the display initially
oled.clear_display()

# Write at a specific line. There are 8 lines with 22 characters available

# Position top left
oled.write_line(0, 0, "Welcome!")

# Position bottom left
oled.write_line(7, 0, "COPYRIGHT 2023")

input("Press ENTER to clear the first line")

# Clear a specific line
oled.write_line(0, 0, " " * 22)

input("Press ENTER to clear the whole display")

# Clear the whole display
oled.clear_display()

# Set all pixels to white
WIDTH = 128 # Columns
HEIGHT = 64 # Rows
oled.write_pixels(0, 0, WIDTH - 1, HEIGHT -1, [1] * WIDTH * HEIGHT)

input("Press ENTER to clear the display again")

oled.clear_display()

# A function to set a specific pixel to white (1) or black (0)
def set_pixel(x, y, color = 1):
    oled.write_pixels(x, y, x, y, [color])

# Draw a diagonal line using this function
y = 0
for x in range(128):
    set_pixel(x, y)

    if x % 2 != 0:
        y = y + 1