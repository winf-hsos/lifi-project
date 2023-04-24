# See: https://lifi.datalit.de/lifi-project/sensing-light
import yaml
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

# Read the current measurements (pull principle)
current_color = color_sensor.get_color()
print(f"Current color: R: { current_color.r }, G: { current_color.g } / B: { current_color.b }")
# Output (example): Current color: R: 22651, G: 24595 / B: 19106

current_illuminance = color_sensor.get_illuminance()
print(f"Current illuminance: { current_illuminance }")
# Output (example): Current illuminance: 17482

current_color_temperature = color_sensor.get_color_temperature()
print(f"Current color temperature: { current_color_temperature }")
# Output (example): Current color temperature: 5097

input("Press ENTER to start working with callback functions.\n")

# Define a callback function for new color values
def new_color_value(r, g, b, c):
    print(f"R: { r }, G: { g }, B: { b }, C: { c }")

# Define a callback function for new color temperature values
def new_color_temperature_value(color_temp):
    print(f"Color temperature: { color_temp }")

# Define a callback function for new illuminance values
def new_illuminance_value(illuminance):
    print(f"Illuminance: { illuminance }")

# Register a callback function for new color values
color_sensor.register_callback(BrickletColorV2.CALLBACK_COLOR, new_color_value)

# Configure the color callback interval to 1 second = 1000 ms and that the value need not change
color_sensor.set_color_callback_configuration(1000, False)

# Register a callback function for new color temperature values
color_sensor.register_callback(BrickletColorV2.CALLBACK_COLOR_TEMPERATURE, new_color_temperature_value)

# Configure the color temperature callback interval to 1 seond = 1000 ms and that the value need not change
color_sensor.set_color_temperature_callback_configuration(1000, False, "x", 0, 0)

# Register a callback function for new illuminance values
color_sensor.register_callback(BrickletColorV2.CALLBACK_ILLUMINANCE, new_illuminance_value)

# Configure the illuminance callback interval to 1 seond = 1000 ms and that the value need not change
color_sensor.set_illuminance_callback_configuration(1000, False, "x", 0, 0)

# Switch on the LED of the sensor
color_sensor.set_light(True)

input("Press ENTER to turn of the sensor's LED.\n")

# Switch of the LED of the sensor
color_sensor.set_light(False)

input("Press ENTER to exit!\n")