import yaml
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
from tinkerforge.bricklet_color_v2 import BrickletColorV2
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

# Load the configuration file
with open('./config.yaml', 'r') as f:
    config = yaml.safe_load(f)

UID_RGB_LED = config.get("uid_rgb_led")
UID_COLOR_SENSOR = config.get("uid_color_sensor")
UID_OLED_DISPLAY = config.get("uid_oled_display")
HOST = config.get("host")
PORT = config.get("port")

# Create IP-connection
ipcon = IPConnection()
ipcon.connect(HOST, PORT)

# Create LED object
led = BrickletRGBLEDV2(UID_RGB_LED, ipcon)
# Create color sensor object
color = BrickletColorV2(UID_COLOR_SENSOR)
# Create OLED display object
oled = BrickletOLED128x64V2(UID_OLED_DISPLAY)

# TODO: Repeatedly ask the user for a text message with only ASCII characters

# TODO: Convert the input to binary

# TODO: Transmit the binary representation using the LED and the three-color protocol

# TODO: Continuously receive signals using the color sensor and decode the signal to bits. When the bit stream is complete, convert to ASCII.

# TODO: Print the received text message to the OLED display