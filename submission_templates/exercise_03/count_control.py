# See: https://github.com/winf-hsos/lifi-exercises/raw/main/exercises/03_exercise_on_and_off.pdf

#region Boilerplate code to connect to device
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

#endregion

# Your code follows here...