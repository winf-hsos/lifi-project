from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
from tinkerforge.bricklet_color_v2 import BrickletColorV2
import time

class LiFiDevice:
    # Constants for callback types
    SEND_LOG = "send_log"
    RECEIVE_LOG = "receive_log"

    def __init__(self, master_brick_uid):
        self.master_brick_uid = master_brick_uid
        
        self.led = None
        self.color_sensor = None
        self.current_color = "off"
        self.received_bits = ""
        self.callback_send_log = None
        self.callback_receive_log = None
 
    def register_callback(self, callback, callback_type=SEND_LOG):
        if callback_type == self.SEND_LOG:
            self.callback_send_log = callback
        elif callback_type == self.RECEIVE_LOG:
            self.callback_receive_log = callback

    def start(self):
        self.setup_devices()

    def setup_devices(self):
        self.ipcon = IPConnection()
        self.ipcon.connect("localhost", 4223)

        if self.led and self.color_sensor:
            return
        
        def device_found(uid, connected_uid, position, hw_version, fw_version,
                         device_id, enum_type):
            if self.led and self.color_sensor:
                return
            if connected_uid == self.master_brick_uid:
                if device_id == 2128:
                    self.callback_send_log(f"Color Sensor found: UID {uid}", "green")
                    self.color_sensor = BrickletColorV2(uid, self.ipcon)
                    self.color_sensor.set_status_led_config(0)
                    self.color_sensor.set_color_callback_configuration(100, False)
                    self.color_sensor.register_callback(self.color_sensor.CALLBACK_COLOR, self.new_color_value)
                elif device_id == 2127:
                    self.callback_send_log(f"RGB LED found: UID {uid}", "green")
                    self.led = BrickletRGBLEDV2(uid, self.ipcon)
                    self.led.set_rgb_value(0, 0, 0)
                    self.led.set_status_led_config(0)

        self.ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, device_found)
        self.ipcon.enumerate()        

    def new_color_value(self, r, g, b, c):
        detected_color = self.detect_color(r, g, b)

        # Ignore unknown colors to simplify
        if detected_color == "unknown":
            return

        # Check if color changed from previous color
        if detected_color != self.current_color:

            if self.current_color == "off":
                self.callback_receive_log(f"Detected incoming message.", "yellow")

            # When the LED turns off, reset received message and do nothing
            if detected_color == "off":

                received_message = self.decode_received_bits()
                self.callback_receive_log(f"Received message: {received_message}", "yellow")
                self.received_bits = ""
                self.current_color = "off"
                return
            
            self.print_dot(detected_color, "receiving")
            bit = self.color_change_to_bit(self.current_color, detected_color)

            # Only add valid bits
            if bit:
                self.received_bits += bit

                if len(self.received_bits) % 8 == 0:
                    last_byte = self.received_bits[-8:]
                    character = chr(int(last_byte, 2))
                    self.callback_receive_log(f" → Received character: {character} → {last_byte}", "yellow")

        # Remember the detected color for next comparison
        self.current_color = detected_color


    def detect_color(self, r, g, b):
        if r < 5000 and g < 5000 and b < 5000:
            return "off"
        if r > g and r > b:
            return "red"
        if g > r and g > b:
            return "green"
        if b > r and b > g:
            return "blue"
        return "unknown"

    def color_change_to_bit(self, old, new):
        transitions = {
            ("off", "red"): "1", ("off", "blue"): "0",
            ("red", "green"): "1", ("red", "blue"): "0",
            ("green", "red"): "0", ("green", "blue"): "1",
            ("blue", "red"): "1", ("blue", "green"): "0"
        }
        return transitions.get((old, new), "")
    
    def decode_received_bits(self):
        message = ""
        for i in range(0, len(self.received_bits), 8):
            byte = self.received_bits[i:i+8]
            message += chr(int(byte, 2))
        return message

    def send_text(self, text):
        self.callback_send_log(f"Sending: \"{text}\"", "yellow")
        for char in text:
            ascii_value = ord(char)
            binary = bin(ascii_value)[2:].zfill(8)
            self.callback_send_log(f"{char}: {binary}: ", "yellow", end="")
            for bit in binary:
                self.send_bit(bit)
                time.sleep(0.2)
            self.callback_send_log("")
        self.callback_send_log("Sending complete", "yellow")
        self.led.set_rgb_value(0, 0, 0)

    def send_bit(self, bit):
        colors = {"off": {"1": (255,0,0), "0": (0,0,255)},
                  "red": {"1": (0,255,0), "0": (0,0,255)},
                  "green": {"1": (0,0,255), "0": (255,0,0)},
                  "blue": {"1": (255,0,0), "0": (0,255,0)}}
        current_rgb = self.led.get_rgb_value()
        current_color = self.rgb_to_color(current_rgb)
        next_rgb = colors[current_color][bit]
        self.led.set_rgb_value(*next_rgb)
        self.print_dot(self.rgb_to_color(next_rgb), "sending")

    def rgb_to_color(self, rgb):
        mapping = {(255,0,0): "red", (0,255,0): "green",
                   (0,0,255): "blue", (0,0,0): "off"}
        return mapping.get(rgb, "unknown")

    def print_dot(self, color, send_or_receive_log="sending"):
        if send_or_receive_log == "sending":
            self.callback_send_log("●", color, end="")
        else:
            self.callback_receive_log("●", color, end="")