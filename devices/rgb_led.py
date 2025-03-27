from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

UID_RGB_LED = "<REPLACE_UID>" # Change to your UID
HOST = "localhost" # Change to your host
PORT = 4223 # Change to your port

# Create IP-connection
ipcon = IPConnection()
ipcon.connect(HOST, PORT)

# Create LED object
led = BrickletRGBLEDV2(UID_RGB_LED, ipcon)

# Set to full green color
led.set_rgb_value(0, 255, 0)

# Get current color
current_rgb = led.get_rgb_value()
print(f"The current RGB values are: R = {current_rgb.r}, G = {current_rgb.g}, B = {current_rgb.b}")

input("Please hit ENTER to turn off the LED and exit the program")

# Turn off the LED by setting it to black
led.set_rgb_value(0, 0, 0)

# Disconnect
ipcon.disconnect()