# See: https://github.com/winf-hsos/lifi-exercises/raw/main/exercises/04_exercise_digitizing_the_physical_world.pdf

#region Boilerplate code to connect to device
import yaml
import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color_v2 import BrickletColorV2

# Load the configuration file
with open('./config.yaml', 'r') as f:
    config = yaml.safe_load(f)

UID_COLOR_SENSOR = config.get("uid_color_sensor")
HOST = config.get("host")
PORT = config.get("port")

# Create an IP connection to the Brick Daemon
ipcon = IPConnection()
ipcon.connect(HOST, PORT)

# Get a reference to the color sensor
color_sensor = BrickletColorV2(UID_COLOR_SENSOR, ipcon)

#endregion

def detect_color(r, g, b):
    # TODO: Implement this function
    return "red" # Replace with actual detected color

key = ""
while key != "exit":
    key = input("Please type a color code (r/g/b/y) or 'exit' to leave: ")

    # TODO: Turn LED to the color given by the user

    # Wait to allow LED to change and sensor to measure
    time.sleep(0.1)

    # TODO: Get the color sensor's measurement
   
    # TODO: Implement the detect_color function
    detected_color = detect_color(0, 0, 0) # Replace 0, 0, 0 with actual measurements

    # TODO: Print the detected color to the console
    print(f"The detected color is >{ detected_color }<.")
    # Example ouptput: The detected color is >red<.