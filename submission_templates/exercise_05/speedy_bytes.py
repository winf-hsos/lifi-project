import yaml
import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

# Load the configuration file
with open('./config.yaml', 'r') as f:
    config = yaml.safe_load(f)

UID_RGB_LED = config.get("uid_rgb_led")
HOST = config.get("host")
PORT = config.get("port")

# Create IP-connection
ipcon = IPConnection()
ipcon.connect(HOST, PORT)

# Create LED object
led = BrickletRGBLEDV2(UID_RGB_LED, ipcon)
led.set_rgb_value(255, 0, 0)
color = "red"

# TODO: Get a number between 0 and 255 from the user
number_decimal = 254

# TODO: Convert the number to binary
number_binary = "11111110"

# TODO: Send the single bits using the LED and 3-color protocol
# TODO: Implement the function send_bit
def send_bit(bit):

    global color

    # TODO: Determine the current color of the LED
    

    # TODO: Decide the next color of the LED based on the current color
    # and the value of the bit we want to send
    if color == "red":
        if bit == "1":
            led.set_rgb_value(0, 255, 0)
            color = "green"
        elif bit == "0":
            led.set_rgb_value(0, 0, 255)
            color = "blue"
    elif color == "green":
        if bit == "1":
            led.set_rgb_value(0, 0, 255)
            color = "blue"
        elif bit == "0":
            led.set_rgb_value(255, 0, 0)
            color = "red"
    elif color == "blue":
        if bit == "1":
            led.set_rgb_value(255, 0, 0)
            color = "red"
        elif bit == "0":
            led.set_rgb_value(0, 255, 0)
            color = "green"

# TODO: Call send_bit for every bit in the binary representation
for bit in number_binary:
    send_bit(bit)
    time.sleep(1)

#send_bit("1")
#time.sleep(1)
#send_bit("0")
#time.sleep(1)
#send_bit("1")
#time.sleep(1)
#send_bit("1")