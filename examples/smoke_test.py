import constants
from time import time, sleep

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_master import BrickMaster
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2
from tinkerforge.bricklet_color_v2 import BrickletColorV2
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

ipcon = IPConnection() # Create IP connection
ipcon.connect(constants.HOST, constants.PORT) # Connect to brickd

# Create device instances
led = BrickletRGBLEDV2(constants.UID_RGB_LED, ipcon)
rotary = BrickletRotaryEncoderV2(constants.UID_ROTARY_ENCODER, ipcon)
oled = BrickletOLED128x64V2(constants.UID_OLED_DISPLAY, ipcon)
color = BrickletColorV2(constants.UID_COLOR_SENSOR, ipcon)

def update_oled_with_rgb_color(r, g, b):
    # Write current RGB LED's color to the OLED display
    oled.write_line(0, 0, "RGD LED Color:".ljust(26))
    oled.write_line(1, 0, f"R={r}, G={g}, B={b}".ljust(26))

def update_oled_with_color_measurement(measured_r, measured_g, measured_b):
    oled.write_line(3, 0, "Color Sensor:".ljust(26))
    max_color_intensity = 65535
    oled.write_line(4, 0, f"R={measured_r / max_color_intensity * 255:.0f}, G={measured_g / max_color_intensity * 255:.0f}, B={measured_b / max_color_intensity * 255:.0f}".ljust(26))

# Turn off the RGB LED's status light
led.set_status_led_config(0)

# Get the current color value of the RGB LED Bricklet
current_rgb_colors = led.get_rgb_value()
update_oled_with_rgb_color(current_rgb_colors.r, current_rgb_colors.g, current_rgb_colors.b)

# Get and reset the current count for the Rotary Encoder Bricklet
rotary.reset()
current_rotary_count = rotary.get_count(reset=False)

# Remember which color is currently controlled by the Rotary Encoder Bricklet (0 = "red", 1 = "green", 2 = "blue")
current_controlled_rgb_color_index = 0

# Set a callback function for the Rotary Encoder Bricklet
def rotary_changed_callback(count):
    if count == 0:
        return
    
    # Get the current color from the RGB LED
    current_rgb = led.get_rgb_value()
    current_rgb_list = [current_rgb.r, current_rgb.g, current_rgb.b]

    # Calculate the new RGB color from the Rotary Encoder's count
    global current_controlled_rgb_color_index
    current_rgb_list[current_controlled_rgb_color_index] += count

    if current_rgb_list[current_controlled_rgb_color_index]  > 255:
        current_rgb_list[current_controlled_rgb_color_index] = 255
    elif current_rgb_list[current_controlled_rgb_color_index] < 0:
        current_rgb_list[current_controlled_rgb_color_index] = 0

    led.set_rgb_value(current_rgb_list[0], current_rgb_list[1], current_rgb_list[2])
    update_oled_with_rgb_color(current_rgb_list[0], current_rgb_list[1], current_rgb_list[2])

    rotary.get_count(True)

def rotary_pressed():
    global current_controlled_rgb_color_index
    time_pressed = time()
    
    while rotary.is_pressed():
        sleep(0.01)
    
        duration_pressed = time() - time_pressed
        if duration_pressed >= 2:
            led.set_rgb_value(0, 0, 0)
            update_oled_with_rgb_color(0, 0, 0)
            return

    current_controlled_rgb_color_index += 1
    if current_controlled_rgb_color_index > 2:
        current_controlled_rgb_color_index = 0

def rotary_released():
    pass   

rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_COUNT, rotary_changed_callback)
rotary.set_count_callback_configuration(10, True, "x", 0, 0)

rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_PRESSED, rotary_pressed)
rotary.register_callback(BrickletRotaryEncoderV2.CALLBACK_RELEASED, rotary_released)

# Set up callback functions for the Color Bricklet
def color_changed(r, g, b, c):
    update_oled_with_color_measurement(r, g, b)

# Turn the status LED off to avoid inteference
color.set_status_led_config(0)

color.register_callback(BrickletColorV2.CALLBACK_COLOR, color_changed)
color.set_color_callback_configuration(20, False)

input("Please hit enter to exit")

# Disconnect from Brick Daemon
ipcon.disconnect()