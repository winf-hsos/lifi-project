# See: https://lifi.datalit.de/lifi-project/the-rotary-encoder
import yaml
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2

# Load the configuration file
with open('./config.yaml', 'r') as f:
    config = yaml.safe_load(f)

UID_ROTARY_ENCODER = config.get("uid_rotary_encoder")
HOST = config.get("host")
PORT = config.get("port")

# Create an IP connection to the Brick Daemon
ipcon = IPConnection()
ipcon.connect(HOST, PORT)

# Get a reference to the Rotary Encoder
rotary = BrickletRotaryEncoderV2(UID_ROTARY_ENCODER, ipcon)

# Manually read the current count value
count = rotary.get_count(True)
print(f"The count is:  { count}")

# Define callback function for the 3 events of the rotary encoder
def receive_new_count(count):
    print(f"New count received: { count }")

def button_released():
    print("Button was released")

    # Toggle status LED with button release
    if rotary.get_status_led_config() == 0:
        rotary.set_status_led_config(1)
    else:
        rotary.set_status_led_config(0)

def button_pressed():
    print("Button was pressed")

# Register the count callback function to get new values automatically
rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_COUNT, receive_new_count)
rotary.set_count_callback_configuration(10, True, "x", 0, 0)

# Register the button's callback functions to be notified when someone presses or relesase it
rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_PRESSED, button_pressed)
rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_RELEASED, button_released)

# Turn off the status LED
rotary.set_status_led_config(0)

# Wait for ENTER to exit, so that we can play around with callbacks
input("Press ENTER to exit\n")