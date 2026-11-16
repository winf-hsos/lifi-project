# Source of `lifi_hardware` 0.9.1

This is the complete public part of the module, copied from <https://github.com/winf-hsos/lifi-hardware>. It is the only authority on which functions exist. Do not use methods that are not defined here; the raw Tinkerforge objects are reachable as `lifi.led.raw` and `lifi.sensor.raw`, but beginners should not need them.

```python
"""lifi_hardware: the interface to your LiFi device.

A device carries an RGB LED (the sender) and a colour sensor (the
receiver), both made by Tinkerforge and connected through the Brick
Daemon. This module finds the parts by itself when your program starts
and gives you two handy objects, ``led`` and ``sensor``:

    from lifi_hardware import led, sensor

    led.set_color(255, 0, 0)       # send red
    reading = sensor.read()        # Reading(r, g, b, c)
    led.off()

If you want to decide yourself when to connect and disconnect, use the
class behind them:

    from lifi_hardware import LifiDevice

    lifi = LifiDevice.connect()
    lifi.led.set_color(255, 0, 0)
    reading = lifi.sensor.read()
    lifi.close()

Two settings of the sensor are visible on purpose, because they are the
central trade-off of the project (signal quality against symbol rate):
``set_integration_time()`` and ``set_gain()``. They are not hidden or
abstracted away, and you are meant to turn them.

Everything the device does also goes into a local measurement log
(``lifi_log.jsonl`` in your working folder), one line of JSON per event.
It is the memory of your measurement series and always works, even
without any network.

The raw Tinkerforge interface stays within reach (``led.raw`` and
``sensor.raw``) in case you want to go deeper.

If two devices hang on the same computer (for example at the front, under
the visualizer), each script says which one it means by the UID of its
master brick, which the Brick Viewer shows:

    from lifi_hardware import led, sensor, use_device

    use_device("64SK5w")
    led.set_color(255, 0, 0)

The same works without changing the code through the environment
variable ``LIFI_MASTER=64SK5w``.

For Challenge 1 there are ``sender``, ``receiver`` and ``run_test``: one
file with ``send_symbol``, ``receive_symbol`` and ``calibrate``, the same
for one laptop with both devices and for two laptops with one device each.
How that works: see _challenge.py.
"""

from __future__ import annotations

import json
import os
import time
from typing import NamedTuple, cast

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color_v2 import BrickletColorV2
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2

from ._telemetry import DEFAULT_SERVER, Telemetry, install_error_hook

__version__ = "0.9.1"

# Device identifiers used by Tinkerforge (device_identifier)
_ID_RGB_LED = 2127               # RGB LED Bricklet 2.0
_ID_COLOR = 2128                 # Color Bricklet 2.0

# The sensor knows only these integration times (milliseconds) ...
_INTEGRATION_TIMES = {
    2.4: BrickletColorV2.INTEGRATION_TIME_2MS,
    24: BrickletColorV2.INTEGRATION_TIME_24MS,
    101: BrickletColorV2.INTEGRATION_TIME_101MS,
    154: BrickletColorV2.INTEGRATION_TIME_154MS,
    700: BrickletColorV2.INTEGRATION_TIME_700MS,
}
# ... and these gain factors.
_GAINS = {
    1: BrickletColorV2.GAIN_1X,
    4: BrickletColorV2.GAIN_4X,
    16: BrickletColorV2.GAIN_16X,
    60: BrickletColorV2.GAIN_60X,
}


class Reading(NamedTuple):
    """One sensor reading: red, green, blue and clear (unfiltered).

    All four values are 16-bit numbers (0 to 65535). The clear channel
    measures without a colour filter and is therefore the most sensitive
    one. The values do NOT match the RGB values that were sent, because
    overlapping filters, distance and room light lie in between, so you
    have to calibrate.
    """

    r: int
    g: int
    b: int
    c: int


class _Log:
    """The local measurement log: one JSON line per event.

    The upload companion can hang on through ``sink`` (see _telemetry.py)
    and receives exactly the same entries that are written to the file:
    local first, upload on top.
    """

    def __init__(self, path):
        self.path = path
        self.sink = None

    def write(self, event, **fields):
        record = {"t": round(time.time(), 4), "event": event, **fields}
        if self.path is not None:
            # Append instead of keeping the file open: robust against
            # crashes, and several programs can write to the same log
            # one after the other.
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
        if self.sink is not None:
            self.sink(record)


class Led:
    """The sender: an RGB LED with three channels from 0 to 255."""

    def __init__(self, raw, log):
        self.raw = raw           # the raw Tinkerforge object
        self._log = log
        self.uid = raw.uid_string

    def set_color(self, r: int, g: int, b: int) -> None:
        """Sets the colour. The LED stays on until something else comes.

        Each value goes from 0 (off) to 255 (full), for example
        ``led.set_color(255, 0, 0)`` for red.
        """
        self.raw.set_rgb_value(r, g, b)
        self._log.write("set_color", r=r, g=g, b=b)

    def off(self) -> None:
        """Switches the LED off (the same as set_color(0, 0, 0))."""
        self.set_color(0, 0, 0)

    @property
    def color(self) -> tuple[int, int, int]:
        """The current colour as (r, g, b), read directly from the hardware.

        Handy for checking what is really being sent right now, for
        example after a program was stopped or while looking for a fault.
        """
        return tuple(self.raw.get_rgb_value())


class Sensor:
    """The receiver: a colour sensor with four channels.

    It has two settings. A longer integration time collects more light
    per reading, which gives calmer values but fewer readings per second;
    a higher gain makes weak light visible, and the noise as well. Both
    belong in your measurement log.
    """

    def __init__(self, raw, log):
        self.raw = raw
        self._log = log
        self.uid = raw.uid_string
        # A known starting state, so that measurement series can be
        # compared. Gain 16x, because 60x saturates the clear channel in
        # normally lit rooms even without a signal (measured 2026-09-03).
        # What suits YOUR link, only your own measurement series can tell.
        self._gain = 16
        self._integration_time = 154
        self._apply()
        # The white lamp of the sensor is meant for measuring the colour
        # of OBJECTS and only disturbs our link, so it is switched off.
        self.set_light(False)

    def _apply(self):
        self.raw.set_configuration(_GAINS[self._gain],
                                   _INTEGRATION_TIMES[self._integration_time])
        self._log.write("configure", gain=self._gain,
                        integration_time=self._integration_time)

    @property
    def integration_time(self):
        """The current integration time in milliseconds."""
        return self._integration_time

    @property
    def gain(self):
        """The current gain factor."""
        return self._gain

    def set_integration_time(self, ms: float) -> None:
        """Sets the integration time. Allowed: 2.4, 24, 101, 154, 700 ms."""
        if ms not in _INTEGRATION_TIMES:
            raise ValueError(
                f"There is no integration time of {ms} ms. "
                f"Allowed: {sorted(_INTEGRATION_TIMES)}")
        self._integration_time = ms
        self._apply()

    def set_gain(self, factor: int) -> None:
        """Sets the gain. Allowed: 1, 4, 16, 60."""
        if factor not in _GAINS:
            raise ValueError(f"There is no gain of {factor}x. "
                             f"Allowed: {sorted(_GAINS)}")
        self._gain = factor
        self._apply()

    def set_light(self, on: bool) -> None:
        """Switches the white lamp on the sensor board.

        It is meant for lighting objects (the sensor can also measure the
        colour of surfaces) and is always off at the start. Leave it off
        for the light link, otherwise the receiver dazzles itself and the
        device opposite.
        """
        self.raw.set_light(bool(on))
        self._log.write("set_light", on=bool(on))

    def read(self) -> Reading:
        """Takes one reading and returns it as Reading(r, g, b, c).

        Important: the sensor measures at its own pace, one reading per
        integration time. This call fetches the NEWEST finished reading
        and does not wait. If you read more often than the sensor
        measures, you get the same value several times; new information
        comes at most once per integration time. That is exactly why the
        integration time is a setting: calmer values against fewer
        readings per second.
        """
        r, g, b, c = self.raw.get_color()
        reading = Reading(r, g, b, c)
        self._log.write("read", r=r, g=g, b=b, c=c)
        return reading


def _discover(ipcon, master=None):
    """Asks the Brick Daemon which parts hang on which master brick.

    Returns {master_uid: {device_identifier: uid}}.
    """
    bricks = {}

    def on_enumerate(uid, connected_uid, position, hw_version,
                     fw_version, device_identifier, enumeration_type):
        if enumeration_type == IPConnection.ENUMERATION_TYPE_DISCONNECTED:
            return
        if device_identifier in (_ID_RGB_LED, _ID_COLOR):
            bricks.setdefault(connected_uid, {}).setdefault(device_identifier, uid)

    ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, on_enumerate)
    ipcon.enumerate()
    # Wait briefly until all parts have reported. Once one device is
    # complete, wait a moment longer for others, so that a second
    # device on the same computer is not missed.
    deadline = time.time() + 2.0
    settle = None
    while time.time() < deadline:
        done = _complete(bricks)
        if master is not None and master in done:
            break
        if master is None and done:
            settle = settle or time.time() + 0.3
            if time.time() > settle:
                break
        time.sleep(0.05)
    return bricks


def _complete(bricks):
    """The master bricks that carry both an LED and a sensor."""
    return sorted(m for m, parts in bricks.items()
                  if _ID_RGB_LED in parts and _ID_COLOR in parts)


def find_devices(host="localhost", port=4223):
    """The UIDs of the master bricks of all complete devices on this
    computer, for example ``["64SK5w", "6Bq3Xa"]``."""
    ipcon = IPConnection()
    ipcon.connect(host, port)
    try:
        return _complete(_discover(ipcon))
    finally:
        ipcon.disconnect()


class LifiDevice:
    """Your LiFi device: an LED and a sensor on one master brick."""

    def __init__(self, ipcon, led, sensor, log, telemetry=None, master_uid=None):
        self._ipcon = ipcon
        self.master_uid = master_uid
        self.led = led
        self.sensor = sensor
        self._log = log
        self._telemetry = telemetry

    @classmethod
    def connect(cls, host="localhost", port=4223, log_file="lifi_log.jsonl",
                server=DEFAULT_SERVER, master=None):
        """Connects to the Brick Daemon and finds the LED and the sensor.

        No configuration is needed: the parts report their unique
        identifier (UID) and their type when the program starts. The LED
        and the sensor always come from the same master brick. If several
        devices hang on the computer, ``master`` chooses one by the UID of
        its master brick; without it you get an error instead of a device
        mixed together by chance. ``log_file=None`` switches the local
        measurement log off.

        ``server`` is the course server that also receives the measurement
        log (how and why: see _telemetry.py). Switch it off at any time
        with ``server=None`` or the environment variable
        ``LIFI_SERVER=off``; without the server everything works the same,
        only without the live view.
        """
        log = _Log(log_file)
        ipcon = IPConnection()
        ipcon.connect(host, port)

        bricks = _discover(ipcon, master)
        devices = _complete(bricks)
        if master is not None:
            chosen = master
        elif len(devices) > 1:
            ipcon.disconnect()
            raise RuntimeError(
                f"{len(devices)} devices found, with the master bricks "
                f"{', '.join(devices)}. Choose one: use_device(\"{devices[0]}\") "
                f"before the first use of led or sensor, or "
                f"LifiDevice.connect(master=\"{devices[0]}\").")
        elif devices:
            chosen = devices[0]
        else:
            chosen = next(iter(bricks), None)
        parts = bricks.get(chosen, {})

        missing = [name for ident, name in
                   [(_ID_RGB_LED, "RGB LED Bricklet 2.0"),
                    (_ID_COLOR, "Color Bricklet 2.0")] if ident not in parts]
        if missing:
            ipcon.disconnect()
            if master is not None:
                others = ", ".join(sorted(bricks)) or "none"
                raise RuntimeError(
                    f"Not found at master brick {master}: {', '.join(missing)}. "
                    f"Master bricks with bricklets: {others}.")
            raise RuntimeError(
                f"Not found: {', '.join(missing)}. Is the device plugged "
                f"into USB, and is the Brick Daemon running on "
                f"{host}:{port}?")

        # The upload companion hangs onto the log BEFORE the first event,
        # so that the starting configuration is uploaded as well.
        server = os.environ.get("LIFI_SERVER", server)
        telemetry = None
        if server and str(server).lower() not in ("off", "none", "0"):
            telemetry = Telemetry(server, parts[_ID_RGB_LED],
                                  parts[_ID_COLOR])
            log.sink = telemetry.record

        # Crashes end up in the log as the type of error plus a cleaned
        # message (details and limits: _telemetry.py, at the bottom)
        install_error_hook(log, telemetry)

        led = Led(BrickletRGBLEDV2(parts[_ID_RGB_LED], ipcon), log)
        sensor = Sensor(BrickletColorV2(parts[_ID_COLOR], ipcon), log)
        log.write("connect", led_uid=led.uid, sensor_uid=sensor.uid,
                  master_uid=chosen, version=__version__)
        return cls(ipcon, led, sensor, log, telemetry, master_uid=chosen)

    def close(self):
        """Switches the LED off and closes the connection cleanly."""
        try:
            self.led.off()
        finally:
            self._log.write("close")
            if self._telemetry is not None:
                self._telemetry.close()
            self._ipcon.disconnect()

    # ``with LifiDevice.connect() as lifi:`` cleans up by itself
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


# --- The easy way in -----------------------------------------------------------
# ``from lifi_hardware import led, sensor`` is enough to start with: the two
# objects connect by themselves on their FIRST use and share one device.
# When the program ends, the LED goes off and the connection is closed. If
# you want more control (your own log, say, or two devices), use
# LifiDevice.connect(). Which device they use is decided by use_device() or
# the environment variable LIFI_MASTER; without either, it is the one device
# plugged into the computer.

_shared_device = None
_selected_master = os.environ.get("LIFI_MASTER") or None


def use_device(master_uid):
    """Chooses the device for ``led`` and ``sensor`` by the UID of its
    master brick, for example ``use_device("64SK5w")``. Call it before the
    first use of led or sensor."""
    global _selected_master
    if _shared_device is not None and _shared_device.master_uid != master_uid:
        raise RuntimeError(
            f"led and sensor are already connected to master brick "
            f"{_shared_device.master_uid}. Call use_device() before the "
            f"first use of led or sensor.")
    _selected_master = master_uid


def _device():
    global _shared_device
    if _shared_device is None:
        import atexit
        _shared_device = LifiDevice.connect(master=_selected_master)
        atexit.register(_shared_device.close)
    return _shared_device


class _LazyPart:
    """A placeholder that hooks itself to the real part on first access."""

    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        return getattr(getattr(_device(), self._name), attr)


# For the editor, led and sensor are an Led and a Sensor, so typing "led."
# shows their methods with their descriptions. At run time they stay
# placeholders that connect only on their first use.
led = cast(Led, _LazyPart("led"))
sensor = cast(Sensor, _LazyPart("sensor"))


# Challenge 1: sender, receiver and the test (see _challenge.py). Imported
# at the end, because that file builds on LifiDevice and find_devices.
from ._challenge import (note_received, note_sent, receiver,  # noqa: E402
                         run_test, sender)
```

## `_challenge.py`: sender, receiver and run_test

```python
"""Challenge 1: ``sender``, ``receiver`` and ``run_test``.

In Challenge 1 one device only sends and the other only receives. A team
writes one file with three functions and hands them to ``run_test``:

    from lifi_hardware import sender, receiver, run_test

    COLORS = {"off": (0, 0, 0), "white": (255, 255, 255)}

    def calibrate(readings):
        ...                                   # learn what each symbol looks like

    def send_symbol(name):
        sender.led.set_color(*COLORS[name])

    def receive_symbol():
        r, g, b, c = receiver.sensor.read()
        ...                                   # which symbol was it?
        return "off"

    run_test(send_symbol, receive_symbol, calibrate, symbols=COLORS)

The sensor of the receiving device measures with gain 16x and an
integration time of 154 ms unless you say otherwise. To try other
settings, hand them to run_test (since 0.7.0):

    run_test(send_symbol, receive_symbol, calibrate, symbols=COLORS,
             gain=4, integration_time=101)

run_test sets them on the receiving device before the calibration, so the
calibration and the test measure the same way; on a laptop that only sends,
they are ignored. Every run reports them to the server, and the team cockpit
shows them next to the result. Setting them inside calibrate or
receive_symbol would be too late: the calibration readings are taken before
calibrate is called.

The symbols are the names in COLORS: ``send_symbol`` gets a name,
``calibrate`` gets the readings by name, ``receive_symbol`` returns a name,
and the result names them too. On the way to the server they travel as
numbers (the position in COLORS), so names may be anything you like.
``symbols=len(COLORS)`` still works and numbers the symbols from 0.

The same file works in both set-ups. With both devices on one laptop, the
module asks once which of the two sends, and the test runs step by step on
this laptop. With one device per laptop, the same file runs on both, the
module asks whether this laptop sends or receives, and the course server
keeps the two in step.

Why the server keeps time here: in Challenge 1 only one question counts,
how many symbols you can tell apart without a mistake. Timing does not
matter yet, so the server says when the next symbol comes. From Challenge 2
on, timing is your problem, and the server no longer helps.

The sequence of symbols comes fresh from the server for every run, so
nobody knows it in advance. What was sent and what was recognised is noted
by ``note_sent`` and ``note_received``; only ``run_test`` calls them, so
that your own code cannot decide what counts as sent. Without the server
(no WLAN, practising at home), a run with both devices on one laptop still
works, with a local random sequence, and is clearly marked as a practice
run that does not count.
"""

from __future__ import annotations

import atexit
import json
import os
import random
import secrets
import sys
import time
import urllib.error
import urllib.request
from typing import cast

from . import _GAINS, _INTEGRATION_TIMES, LifiDevice, find_devices
from ._telemetry import DEFAULT_SERVER

_READINGS_PER_SYMBOL = 5     # readings per symbol during calibration
_POLL = 0.15                 # seconds between two questions to the server
_WAIT_FOR_PARTNER = 300      # seconds to wait for the other laptop
_TIMEOUT = 5                 # seconds for one request to the server
_RETRY_FOR = 30              # seconds to keep asking again after a failure
_RETRY_CODES = (502, 503, 504)  # the server is restarting or overloaded


# --- Colours on the console -------------------------------------------------------
#
# Only for looks: ok in green, mistakes in red, and a small block in the colour
# the LED showed. When the output does not go to a console (for example when
# OpenCode reads it) or NO_COLOR is set, everything stays plain text.

def _colour_support():
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    if not getattr(sys.stdout, "isatty", lambda: False)():
        return False
    if os.name == "nt":
        # A Windows console understands colour codes only after being asked
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_uint32()
            if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                return False
            return bool(kernel32.SetConsoleMode(handle, mode.value | 0x0004))
        except Exception:
            return False
    return True


_COLOUR = _colour_support()
_STYLES = {"bold": "1", "dim": "2", "red": "31", "green": "32", "yellow": "33",
           "cyan": "36", "on-green": "42", "on-red": "41"}


def _paint(text, *styles):
    """The text in the given styles, or unchanged without colour support."""
    if not _COLOUR or not styles:
        return text
    return f"\033[{';'.join(_STYLES[s] for s in styles)}m{text}\033[0m"


def _swatch(rgb):
    """Two character cells in the colour (r, g, b), for the console.

    Uses the 256-colour palette, which every common console shows. Off is
    drawn as two dim dashes, because black would vanish on a black console.
    """
    if not _COLOUR or rgb is None:
        return ""
    if tuple(rgb) == (0, 0, 0):
        return _paint("--", "dim") + " "
    r, g, b = (round(v / 255 * 5) for v in rgb)
    return f"\033[48;5;{16 + 36 * r + 6 * g + b}m  \033[0m "


def _heading(title, text, end=""):
    """A step of the test, such as "Calibrating: ...". Without a line break,
    so that the calibration can add one mark per symbol to the same line."""
    print(f"{_paint(title, 'cyan', 'bold')}: {text}", end=end, flush=True)


def _show(run, index, width=0):
    """A symbol for printing, by its name; None (an invalid answer) as a dash.
    ``width`` pads to the longest name, so that the columns stay in line."""
    text = "-" if index is None else str(run.labels[index])
    return text.rjust(width)


def _shown_colour():
    """The colour the sending LED shows right now, if it is on this laptop."""
    if not _COLOUR or not _roles or _roles["sender"] is None:
        return None
    try:
        return _roles["sender"].led.color
    except Exception:
        return None


# --- Who sends, who receives ----------------------------------------------------

_roles = None                # {"sender": LifiDevice or None, "receiver": ...}


def _ask(question, answers):
    """Asks until one of the allowed answers comes back."""
    while True:
        answer = input(question).strip().lower()
        if answer in answers:
            return answer
        print(f"Please answer with {' or '.join(answers)}.")


def _choose_roles():
    """Finds the devices on this laptop and asks which one does what."""
    global _roles
    if _roles is not None:
        return _roles
    masters = find_devices()
    if not masters:
        raise RuntimeError(
            "No device found. Is it plugged into USB, and is the Brick "
            "Daemon running?")

    if len(masters) == 1:
        device = LifiDevice.connect(master=masters[0])
        atexit.register(device.close)
        print(f"One device on this laptop ({masters[0]}).")
        answer = _ask("Does this laptop send (s) or receive (r)? ", ["s", "r"])
        _roles = ({"sender": device, "receiver": None} if answer == "s"
                  else {"sender": None, "receiver": device})
        return _roles

    # Two or more devices: each gets its own measurement log, otherwise
    # the readings of both would end up mixed in one file.
    devices = {m: LifiDevice.connect(master=m, log_file=f"lifi_log_{m}.jsonl")
               for m in masters}
    for device in devices.values():
        atexit.register(device.close)
    if len(masters) == 2:
        first, second = masters
        devices[first].led.set_color(255, 255, 255)
        print(f"Two devices on this laptop: {first} and {second}.")
        answer = _ask("The device whose LED is on now: does it send (s) "
                      "or receive (r)? ", ["s", "r"])
        devices[first].led.off()
        sending, receiving = (first, second) if answer == "s" else (second, first)
    else:
        print("Devices on this laptop:")
        for number, master in enumerate(masters, start=1):
            print(f"  {number}  {master}")
        numbers = [str(n) for n in range(1, len(masters) + 1)]
        sending = masters[int(_ask("Number of the device that sends: ", numbers)) - 1]
        receiving = masters[int(_ask("Number of the device that receives: ", numbers)) - 1]
        if sending == receiving:
            raise RuntimeError("Sender and receiver have to be two different devices.")
    print(f"Sender: {_paint(sending, 'bold')}, receiver: {_paint(receiving, 'bold')}")
    _roles = {"sender": devices[sending], "receiver": devices[receiving]}
    return _roles


class _Role:
    """``sender`` or ``receiver``: the device in that role, found on first use."""

    def __init__(self, name):
        self._name = name

    def _device(self):
        device = _choose_roles()[self._name]
        if device is None:
            other = "receiver" if self._name == "sender" else "sender"
            raise RuntimeError(
                f"This laptop is the {other}. The {self._name} is the device "
                f"on the other laptop, so {self._name}.led and "
                f"{self._name}.sensor do not exist here.")
        return device

    def __getattr__(self, attr):
        return getattr(self._device(), attr)


# For the editor, sender and receiver are LifiDevices, so "sender." offers
# led and sensor. At run time they are placeholders that decide on first use.
sender = cast(LifiDevice, _Role("sender"))
receiver = cast(LifiDevice, _Role("receiver"))


# --- Talking to the server ------------------------------------------------------

class ServerError(RuntimeError):
    """The server answered, but with a refusal (the reason is the message)."""


def _server():
    url = os.environ.get("LIFI_SERVER", DEFAULT_SERVER)
    if not url or str(url).lower() in ("off", "none", "0"):
        return None
    return url.rstrip("/")


def _api_once(method, path, body):
    request = urllib.request.Request(
        _server() + path, method=method,
        data=None if body is None else json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=_TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8"))


def _api(method, path, body=None):
    """One request to the course server, asked again after a short failure.

    In a room with forty laptops in one WLAN, a request now and then gets no
    answer in time. Since 0.8.1 that no longer ends the run: the module
    waits a moment and asks again, for up to ``_RETRY_FOR`` seconds. Asking
    twice is safe, because the server recognises a repeated message (the
    same position, the same ``join_id``) and does not count it twice.
    A refusal (the server answered, but said no) is not asked again.
    """
    started = time.time()
    pause = 0.5
    told = False
    while True:
        try:
            return _api_once(method, path, body)
        except urllib.error.HTTPError as error:
            if error.code not in _RETRY_CODES:
                try:
                    detail = json.loads(error.read().decode("utf-8")).get("detail")
                except (ValueError, AttributeError):
                    detail = None
                raise ServerError(detail or f"the server answered {error.code}") from None
            failure = error
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            failure = error
        if time.time() - started + pause > _RETRY_FOR:
            if isinstance(failure, urllib.error.HTTPError):
                raise ServerError(f"the server answered {failure.code}") from None
            raise failure
        if not told:
            print(_paint("  the course server did not answer in time, asking again ...",
                         "dim"))
            told = True
        time.sleep(pause)
        pause = min(pause * 2, 4)


# --- Noting what was sent and received ------------------------------------------

class _Run:
    """One run of run_test: on the server, or locally as a practice run.

    Inside, every symbol is its number (its position in the alphabet), and
    so it travels to the server. ``labels`` are the names your functions
    see: the names in COLORS, or 0, 1, 2, ... with ``symbols=len(COLORS)``.
    """

    def __init__(self, role, labels, runs, practice, run_id=None):
        self.role = role
        self.labels = labels
        self.symbols = len(labels)
        self.width = max(len(str(label)) for label in labels)
        self.runs = runs
        self.practice = practice
        self.id = run_id
        self.sequence = None         # known locally only in a practice run
        self.received = []


def _labels(symbols):
    """The names of the symbols: a number gives 0 to n-1, a dictionary such
    as COLORS gives its keys, a list gives its entries."""
    if isinstance(symbols, bool):
        raise TypeError("symbols has to be your alphabet, for example "
                        "run_test(..., symbols=COLORS)")
    if isinstance(symbols, int):
        labels = list(range(symbols))
    else:
        try:
            labels = list(symbols)
        except TypeError:
            raise TypeError("symbols has to be your alphabet, for example "
                            "run_test(..., symbols=COLORS)") from None
    if len(labels) < 2:
        raise ValueError("An alphabet needs at least two symbols.")
    if len(set(map(str, labels))) != len(labels):
        raise ValueError("Every symbol in the alphabet needs its own name.")
    return labels


def note_sent(run, position, symbol):
    """Notes that ``symbol`` now shows at ``position`` of the run.

    Called by run_test only, never by your own code: what counts as sent
    is decided by the test, not by the program being tested. The note goes
    into the measurement log of the sending device and to the server.
    """
    device = _roles["sender"]
    device._log.write("note_sent", run=run.id, position=position, symbol=symbol,
                      name=str(run.labels[symbol]))
    if not run.practice:
        return _api("POST", f"/api/runs/{run.id}/sent",
                    {"role": run.role, "position": position, "symbol": symbol})


def note_received(run, position, symbol):
    """Notes which symbol the receiver recognised at ``position``.

    Called by run_test only. During calibration ``symbol`` is None. The note
    goes into the measurement log of the receiving device and to the server.
    """
    device = _roles["receiver"]
    device._log.write("note_received", run=run.id, position=position,
                      symbol=symbol,
                      name=None if symbol is None else str(run.labels[symbol]))
    if not run.practice:
        return _api("POST", f"/api/runs/{run.id}/received",
                    {"role": run.role, "position": position, "symbol": symbol})


# --- The test -------------------------------------------------------------------

def _settle_time():
    """How long a new symbol has to stand before a reading shows it.

    The sensor hands out its newest FINISHED reading. Right after a change,
    that reading may still have begun before it, so we wait for two full
    integration times.
    """
    return 2 * receiver.sensor.integration_time / 1000 + 0.05


def _measure_calibration():
    """A few readings of the symbol that is showing right now."""
    pause = receiver.sensor.integration_time / 1000
    readings = []
    for _ in range(_READINGS_PER_SYMBOL):
        readings.append(receiver.sensor.read())
        time.sleep(pause)
    return readings


def _check(run, answer):
    """The number of the symbol receive_symbol() named, or None if it named
    none of the alphabet (that counts as a mistake)."""
    for index, label in enumerate(run.labels):
        if type(answer) is type(label) and answer == label:
            return index
    if all(isinstance(label, int) for label in run.labels):
        expected = f"a whole number from 0 to {run.symbols - 1}"
    else:
        expected = "one of the names in your alphabet: " + ", ".join(
            repr(label) for label in run.labels)
    print(_paint(f"  receive_symbol() returned {answer!r}, but it has to return "
                 f"{expected}. Counted as a mistake.", "yellow"))
    return None


def _wait(run, until, what):
    """Asks the server until ``until(state)`` holds and returns that state."""
    started = time.time()
    shown = False
    while True:
        state = _api("GET", f"/api/runs/{run.id}?role={run.role}")
        if until(state):
            return state
        if not shown and time.time() - started > 2:
            print(_paint(f"  waiting for {what} ...", "dim"))
            shown = True
        if time.time() - started > _WAIT_FOR_PARTNER:
            raise RuntimeError(f"Waited {_WAIT_FOR_PARTNER} s for {what}. "
                               f"Start run_test again on both laptops.")
        time.sleep(_POLL)


def run_test(send_symbol, receive_symbol, calibrate=None, symbols=None,
             runs=20, team=None, gain=None, integration_time=None,
             codebook=None, sentences=3, text=None):
    """The test for Challenge 1: how many symbols get through without a mistake?

    With a ``codebook`` it is the test for Challenge 2 instead (since
    0.9.0): then the first two arguments are ``send_text`` and
    ``receive_text``, and ``sentences`` says how many sentences one run
    sends (3 count for the challenge). How that works: see _word.py.
    ``text="HELLO WORLD"`` (since 0.9.1) sends your own text instead, as a
    quick practice run with both devices on one laptop that does not count;
    a list of texts sends one after the other.

    ``symbols`` is your alphabet, usually ``COLORS``: its names are the
    symbols. ``send_symbol(name)`` shows the symbol with that name.
    ``receive_symbol()`` measures and returns the name of the symbol it
    recognised. ``calibrate(readings)`` is called once before the test,
    after the whole alphabet has been shown once: ``readings`` is a
    dictionary from each name to a list of Readings taken while that symbol
    was showing, so ``readings["white"]``. What you make of them is up to you.

    With ``symbols=len(COLORS)``, as in the first version of the template,
    the symbols are the numbers 0 to ``len(COLORS) - 1`` instead of names.

    ``team`` is needed only if your devices are not registered with a team
    yet: then both laptops find each other by this name, and the run does
    not count.

    ``gain`` (1, 4, 16 or 60) and ``integration_time`` (2.4, 24, 101, 154 or
    700 milliseconds) set the sensor of the receiving device before the
    calibration. Without them it measures with 16x and 154 ms, as after
    every start. A laptop that only sends ignores them.

    Returns a dictionary with the number of hits, the two sequences by name
    and the sensor settings of the receiver.
    """
    if symbols is None:
        raise TypeError("run_test needs your alphabet, for example "
                        "run_test(..., symbols=COLORS)")
    # Check the settings first, so that a typo stops BOTH laptops before
    # anything happens, not only the receiving one halfway through
    if gain is not None and gain not in _GAINS:
        raise ValueError(f"There is no gain of {gain}x. "
                         f"Allowed: {sorted(_GAINS)}")
    if integration_time is not None and integration_time not in _INTEGRATION_TIMES:
        raise ValueError(f"There is no integration time of {integration_time} ms. "
                         f"Allowed: {sorted(_INTEGRATION_TIMES)}")
    if codebook is not None:
        from ._word import run_word_test
        return run_word_test(send_symbol, receive_symbol, calibrate, symbols,
                             codebook, sentences=sentences, team=team, gain=gain,
                             integration_time=integration_time, text=text)
    if text is not None:
        raise TypeError("text only works in Challenge 2, together with "
                        "codebook=CODEBOOK.")
    labels = _labels(symbols)
    roles = _choose_roles()
    role = ("both" if roles["sender"] and roles["receiver"]
            else "sender" if roles["sender"] else "receiver")
    some_device = roles["sender"] or roles["receiver"]

    settings = {}
    if roles["receiver"] is not None:
        sensor = roles["receiver"].sensor
        if gain is not None:
            sensor.set_gain(gain)
        if integration_time is not None:
            sensor.set_integration_time(integration_time)
        settings = {"gain": sensor.gain, "integration_time": sensor.integration_time}

    run = _start(role, labels, runs, team, some_device, settings,
                 _alphabet(symbols, labels))
    if settings:
        print(f"Sensor of the receiver: gain {settings['gain']}x, "
              f"integration time {settings['integration_time']} ms.")
    try:
        if role == "both":
            _run_both(run, send_symbol, receive_symbol, calibrate)
        elif role == "sender":
            _run_sender(run, send_symbol)
        else:
            _run_receiver(run, receive_symbol, calibrate)
    finally:
        if roles["sender"] is not None:
            roles["sender"].led.off()
    return {**_report(run), **settings}


def _color(value):
    """A colour from the alphabet as [r, g, b] with 0 to 255, or None if it
    is written in a way this function does not know. Only for showing the
    alphabet in the cockpit and on the projector, never for the test."""
    try:
        if isinstance(value, str):
            text = value.strip().lstrip("#")
            if len(text) == 6:
                return [int(text[i:i + 2], 16) for i in (0, 2, 4)]
            return None
        parts = list(value)
        if len(parts) != 3:
            return None
        rgb = [int(round(float(x))) for x in parts]
        return rgb if all(0 <= x <= 255 for x in rgb) else None
    except (TypeError, ValueError):
        return None


def _alphabet(symbols, labels):
    """Names and colours of the alphabet for the server (since 0.8.0), so the
    projector view during an acceptance test can show the real colours."""
    colors = symbols if isinstance(symbols, dict) else {}
    return [{"name": str(label)[:40], "color": _color(colors.get(label))}
            for label in labels]


def _start(role, labels, runs, team, device, settings=None, alphabet=None):
    """Asks the server for a new run, or falls back to a practice run."""
    symbols = len(labels)
    if _server() is not None:
        try:
            payload = {
                "role": role, "led_uid": device.led.uid,
                "sensor_uid": device.sensor.uid,
                "master_uid": device.master_uid, "team": team,
                "symbols": symbols, "runs": runs,
                # the same id on every retry, so the server hands out the
                # same run instead of a second one (since 0.8.1)
                "join_id": secrets.token_urlsafe(12), **(settings or {})}
            if alphabet:
                payload["alphabet"] = alphabet
            state = _api("POST", "/api/runs/join", payload)
            run = _Run(role, labels, runs, practice=False, run_id=state["run_id"])
            note = (_paint("counts", "green") if state["counted"] else
                    _paint("does NOT count (devices not registered)", "yellow"))
            print(f"Run for {_paint(state['team'], 'bold')}: {symbols} symbols, "
                  f"{runs} runs, this run {note}.")
            return run
        except (urllib.error.URLError, TimeoutError, OSError):
            pass
    if role != "both":
        raise RuntimeError(
            "The course server cannot be reached. With two laptops, the server "
            "keeps the two in step, so this does not work offline. Check the "
            "WLAN, or plug both devices into one laptop for a practice run.")
    print(_paint("The course server cannot be reached: PRACTICE RUN, it does not count.",
                 "yellow"))
    run = _Run(role, labels, runs, practice=True, run_id="practice")
    rng = random.SystemRandom()
    run.sequence = [rng.randrange(symbols) for _ in range(runs)]
    return run


def _steps(run):
    """The steps of a practice run, in the same order as on the server."""
    return ([("calibrate", i) for i in range(run.symbols)]
            + [("test", s) for s in run.sequence])


def _run_both(run, send_symbol, receive_symbol, calibrate):
    """Both devices on this laptop: send, wait, measure, note, next."""
    _heading("Calibrating", "showing the whole alphabet once ")
    readings = {}
    position = 0
    while True:
        if run.practice:
            if position >= run.symbols + run.runs:
                return
            phase, symbol = _steps(run)[position]
        else:
            state = _api("GET", f"/api/runs/{run.id}?role=both")
            if state["state"] == "done":
                run.state = state
                return
            phase, symbol = state["phase"], state["symbol"]
        if phase == "test" and position == run.symbols:
            print()
            if calibrate is not None:
                calibrate(readings)
            _heading("Testing", f"{run.runs} symbols", end="\n")
        send_symbol(run.labels[symbol])
        time.sleep(_settle_time())
        note_sent(run, position, symbol)
        if phase == "calibrate":
            readings[run.labels[symbol]] = _measure_calibration()
            note_received(run, position, None)
            print(_swatch(_shown_colour()) or ".", end="", flush=True)
        else:
            got = _check(run, receive_symbol())
            run.received.append(got)
            note_received(run, position, got)
            mark = _paint("ok", "green") if got == symbol else _paint("MISTAKE", "red", "bold")
            print(f"  {position - run.symbols + 1:>3}/{run.runs}  sent "
                  f"{_show(run, symbol, run.width)} {_swatch(_shown_colour())}"
                  f"recognised {_show(run, got, run.width)}  {mark}")
        position += 1


def _run_sender(run, send_symbol):
    """This laptop only sends; the server says what and when."""
    _wait(run, lambda s: s["state"] != "waiting", "the receiving laptop")
    _heading("Calibrating", "showing the whole alphabet once ")
    while True:
        state = _wait(run, lambda s: s["state"] == "done" or not s["sent"],
                      "the receiver")
        if state["state"] == "done":
            run.state = state
            return
        position, symbol = state["position"], state["symbol"]
        if state["phase"] == "test" and position == run.symbols:
            print()
            _heading("Testing", f"{run.runs} symbols", end="\n")
        send_symbol(run.labels[symbol])
        time.sleep(0.1)
        note_sent(run, position, symbol)
        if state["phase"] == "test":
            print(f"  {position - run.symbols + 1:>3}/{run.runs}  sent "
                  f"{_show(run, symbol, run.width)} {_swatch(_shown_colour())}".rstrip())
        else:
            print(_swatch(_shown_colour()) or ".", end="", flush=True)
        # Wait until the receiver has measured, then the next symbol comes
        _wait(run, lambda s: s["state"] == "done" or s["position"] > position,
              "the receiver")


def _run_receiver(run, receive_symbol, calibrate):
    """This laptop only receives; it measures whenever the sender is ready."""
    _wait(run, lambda s: s["state"] != "waiting", "the sending laptop")
    _heading("Calibrating", "measuring the whole alphabet once ")
    readings = {}
    while True:
        state = _wait(run, lambda s: s["state"] == "done" or s["sent"],
                      "the sender")
        if state["state"] == "done":
            run.state = state
            return
        position = state["position"]
        time.sleep(_settle_time())
        if state["phase"] == "calibrate":
            readings[run.labels[state["symbol"]]] = _measure_calibration()
            note_received(run, position, None)
            print(".", end="", flush=True)
            continue
        if position == run.symbols:
            print()
            if calibrate is not None:
                calibrate(readings)
            _heading("Testing", f"{run.runs} symbols", end="\n")
        got = _check(run, receive_symbol())
        run.received.append(got)
        result = note_received(run, position, got)
        print(f"  {position - run.symbols + 1:>3}/{run.runs}  recognised "
              f"{_show(run, got, run.width)}")
        if result and result["state"] == "done":
            run.state = result
            return


def _report(run):
    """Prints the result and where the mistakes were."""
    if run.practice:
        sequence, received = run.sequence, run.received
    else:
        state = getattr(run, "state", None) or _api(
            "GET", f"/api/runs/{run.id}?role={run.role}")
        sequence, received = state["sequence"], state["received"]
    hits = sum(1 for a, b in zip(sequence, received) if a == b)
    print()
    # One cell per attempt: green for a hit, red for a mistake (+ and x
    # without colour support)
    if _COLOUR:
        hit, miss = _paint(" ", "on-green"), _paint(" ", "on-red")
    else:
        hit, miss = "+", "x"
    cells = " ".join(hit if a == b else miss for a, b in zip(sequence, received))
    print(f"  {cells}")
    kind = "Practice run" if run.practice else "Result"
    perfect = hits == run.runs
    print(_paint(f"{kind}: {hits} of {run.runs} recognised with {run.symbols} symbols.",
                 "bold", "green" if perfect else "red"))
    mistakes = [(i + 1, a, b) for i, (a, b) in enumerate(zip(sequence, received))
                if a != b]
    if mistakes:
        print("Mistakes (position: sent -> recognised):")
        for position, sent, got in mistakes:
            print(f"  {position:>3}: {_show(run, sent, run.width)} -> "
                  f"{_paint(_show(run, got), 'red')}")
        # The most common mix-up; answers outside the alphabet are no mix-up
        pairs = {}
        for _, sent, got in mistakes:
            if got is not None:
                pairs[(sent, got)] = pairs.get((sent, got), 0) + 1
        common = max(pairs.items(), key=lambda item: item[1], default=(None, 0))
        if common[1] > 1:
            (sent, got), count = common
            print(_paint(f"{_show(run, sent)} was taken for {_show(run, got)} {count} "
                         f"times: these two are probably too close together.", "yellow"))
    else:
        print(_paint("No mistakes.", "green"))
    if run.practice:
        print(_paint("This was a practice run; it does not count.", "yellow"))

    def name(index):
        return None if index is None else run.labels[index]

    return {"hits": hits, "runs": run.runs, "symbols": run.symbols,
            "sequence": [name(i) for i in sequence],
            "received": [name(i) for i in received],
            "practice": run.practice}
```

## `_word.py`: run_test with a codebook (Challenge 2)

```python
"""Challenge 2: ``run_test`` with a ``codebook``.

In Challenge 2 a team sends whole sentences. The file of Challenge 1 grows
by a CODEBOOK (which colours stand for which character) and two functions,
``send_text(text)`` and ``receive_text(n_chars)``; the last line becomes

    run_test(send_text, receive_text, calibrate, symbols=COLORS,
             codebook=CODEBOOK, gain=GAIN, integration_time=INTEGRATION_TIME)

Giving a ``codebook`` is what tells run_test that this is Challenge 2.

A run has four parts: a calibration and three sentences. Each sentence is
three real words in capital letters with a space between them, drawn fresh
by the course server for every run, such as "BUSY FROGS DANCE". The sender
gets the sentence, the receiver only the number of characters.

The server gives each part a common start and nothing else. From the start
on, the code of the team keeps time: run_test calls ``send_text`` on the
sending device and ``receive_text`` on the receiving one at the same moment
and measures how long ``send_text`` takes. When it returns, the LED goes
off. With both devices on one laptop, both functions run side by side on
this laptop. With two laptops, each laptop asks the server for its clock a
few times and turns the start into its own clock; the two starts then agree
to within a few hundredths of a second, not exactly.

For the calibration, run_test shows every colour of COLORS once, a fixed
time each, with the values written in COLORS, and the receiver takes a few
readings of each. Then it calls ``calibrate(readings)`` as in Challenge 1.

A run counts when all three sentences arrive without a single mistake. Its
speed is the number of characters divided by the time ``send_text`` took,
in characters per second. Next to it stands the measured symbol rate, all
colours sent divided by the same time, and from it bits per second: the
symbol rate times log2 of the number of colours.

For a quick test in between, ``text="HELLO WORLD"`` sends your own text
instead of the sentences of the server (a list sends several, one after the
other). That is always a practice run with both devices on one laptop: it
does not ask the server and does not count.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import secrets
import threading
import time
import urllib.error

from . import _challenge as c

CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "   # every character a sentence can hold
_HEARTBEAT = 2.0      # seconds between two signs of life during a long part
_LEAD = 1.5           # seconds between "ready" and the start in a practice run

# The words of a practice run; the course server has the same lists
_WORDS = (
    ("RED", "BLUE", "GREEN", "OLD", "YOUNG", "BIG", "SMALL", "TINY", "HAPPY",
     "SHY", "LOUD", "QUIET", "BRAVE", "LAZY", "WILD", "CALM", "FAST", "SLOW",
     "WARM", "COLD", "BUSY", "SILLY", "WISE", "PROUD", "NEAT", "BOLD", "KIND",
     "FUNNY", "SWEET", "GRAY"),
    ("CATS", "DOGS", "FOXES", "BIRDS", "BEARS", "FROGS", "BEES", "OWLS",
     "GOATS", "COWS", "MICE", "DUCKS", "FISH", "KIDS", "BOTS", "CHEFS",
     "KINGS", "CROWS", "ANTS", "BATS", "PIGS", "HENS", "SEALS", "CRABS",
     "LIONS", "MOLES", "YAKS", "MOTHS", "TOADS", "WORMS"),
    ("RUN", "JUMP", "SING", "DANCE", "SLEEP", "SWIM", "FLY", "LAUGH", "READ",
     "COOK", "PLAY", "HIDE", "WAIT", "SMILE", "BARK", "DREAM", "CLAP", "SHOUT",
     "WAVE", "DIVE", "ROAR", "HUM", "NAP", "SPIN", "HOP", "CHAT", "SKIP",
     "YAWN", "BLINK", "WALK"),
)


# --- Checking the codebook before anything happens ------------------------------

def _check_codebook(codebook, labels):
    """Stops with a clear message if the codebook cannot work, on both
    laptops, before the run starts. Returns the colours of each character."""
    if not isinstance(codebook, dict):
        raise TypeError("codebook has to be your CODEBOOK: a dictionary from "
                        "each character to a list of colour names")
    missing = [ch for ch in CHARSET if ch not in codebook]
    if missing:
        shown = ", ".join("the space" if ch == " " else ch for ch in missing)
        raise ValueError(f"Your CODEBOOK has no entry for {shown}. Every letter "
                         f"from A to Z and the space need one.")
    known = set(labels)
    seen = {}
    for ch in CHARSET:
        colours = codebook[ch]
        if isinstance(colours, str) or not isinstance(colours, (list, tuple)) \
                or not colours:
            raise ValueError(f"CODEBOOK[{ch!r}] has to be a list of colour names "
                             f"from COLORS, for example [\"off\", \"white\"].")
        for name in colours:
            if name not in known:
                raise ValueError(f"CODEBOOK[{ch!r}] uses {name!r}, which is not a "
                                 f"colour in COLORS.")
        key = tuple(colours)
        if key in seen:
            print(c._paint(f"Note: {seen[key]!r} and {ch!r} have the same colours in "
                           f"CODEBOOK, so the receiver cannot tell them apart.",
                           "yellow"))
        seen.setdefault(key, ch)


def _codebook_id(codebook):
    """A fingerprint of the codebook, so the server can tell whether both
    laptops run the same file."""
    text = json.dumps({str(k): [str(x) for x in v] for k, v in codebook.items()},
                      sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _rgb_values(symbols, labels):
    """The LED values of every colour, for the calibration."""
    if not isinstance(symbols, dict):
        raise TypeError("In Challenge 2, symbols has to be your COLORS, so that "
                        "run_test can show every colour for the calibration.")
    values = {}
    for label in labels:
        rgb = c._color(symbols[label])
        if rgb is None:
            raise ValueError(f"COLORS[{label!r}] has to be three numbers from 0 to "
                             f"255, for example (255, 0, 0).")
        values[label] = rgb
    return values


# --- Time -----------------------------------------------------------------------

def _clock_offset():
    """How far the clock of the server is ahead of this laptop, in seconds.

    Asks a few times and keeps the answer that came back fastest: the
    shorter the way, the less it can be off."""
    best = None
    for _ in range(5):
        before = time.time()
        try:
            now = c._api_once("GET", "/api/time", None)["now"]
        except Exception:
            continue
        after = time.time()
        if best is None or after - before < best[0]:
            best = (after - before, now - (before + after) / 2)
    if best is None:
        return c._api("GET", "/api/time")["now"] - time.time()
    return best[1]


def _sleep_until(moment):
    left = moment - time.time()
    if left > 0:
        time.sleep(left)


def _slot(integration_time):
    """How long each colour shows during the calibration (as on the server)."""
    return round(7 * integration_time / 1000 + 0.5, 3)


class _Heartbeat:
    """Tells the server now and then that this laptop is still there, while
    send_text or receive_text take their time. Without it, a long sentence
    would look like a laptop that has gone silent."""

    def __init__(self, run):
        self.run = run
        self.stopped = None
        self._stop = threading.Event()
        self._thread = None

    def __enter__(self):
        if not self.run.practice:
            self._thread = threading.Thread(target=self._beat, daemon=True)
            self._thread.start()
        return self

    def __exit__(self, *exc):
        self._stop.set()
        return False

    def _beat(self):
        while not self._stop.wait(_HEARTBEAT):
            try:
                c._api_once("GET", f"/api/runs/{self.run.id}?role={self.run.role}", None)
            except urllib.error.HTTPError as error:
                if error.code in (404, 410):
                    try:
                        self.stopped = json.loads(error.read().decode("utf-8")).get("detail")
                    except (ValueError, AttributeError):
                        self.stopped = "the run has stopped"
                    print(c._paint(f"\n  {self.stopped}", "red"))
                    return
            except Exception:
                pass


# --- The run --------------------------------------------------------------------

def run_word_test(send_text, receive_text, calibrate, symbols, codebook,
                  sentences=3, team=None, gain=None, integration_time=None,
                  text=None):
    """Challenge 2, called by run_test when it gets a ``codebook``."""
    labels = c._labels(symbols)
    _check_codebook(codebook, labels)
    rgb = _rgb_values(symbols, labels)
    texts = _own_texts(text, codebook)
    if texts:
        sentences = len(texts)
    if not isinstance(sentences, int) or not 1 <= sentences <= 10:
        raise ValueError("sentences has to be a whole number from 1 to 10.")
    roles = c._choose_roles()
    role = ("both" if roles["sender"] and roles["receiver"]
            else "sender" if roles["sender"] else "receiver")
    if texts and role != "both":
        raise RuntimeError(
            "A run with your own text needs both devices on this laptop: it is a "
            "practice run without the course server. With two laptops, leave "
            "text= out.")
    some_device = roles["sender"] or roles["receiver"]

    settings = {}
    if roles["receiver"] is not None:
        sensor = roles["receiver"].sensor
        if gain is not None:
            sensor.set_gain(gain)
        if integration_time is not None:
            sensor.set_integration_time(integration_time)
        settings = {"gain": sensor.gain, "integration_time": sensor.integration_time}

    run = _start(role, labels, sentences, team, some_device, settings,
                 c._alphabet(symbols, labels), _codebook_id(codebook), texts)
    run.codebook = codebook
    run.rgb = rgb
    if settings:
        print(f"Sensor of the receiver: gain {settings['gain']}x, "
              f"integration time {settings['integration_time']} ms.")
    try:
        _run(run, send_text, receive_text, calibrate)
    finally:
        if roles["sender"] is not None:
            roles["sender"].led.off()
    return {**_report(run), **settings}


def _own_texts(text, codebook):
    """The texts of a practice run with your own text, checked against the
    codebook; None without text=."""
    if text is None:
        return None
    texts = [text] if isinstance(text, str) else text
    if not isinstance(texts, (list, tuple)) or not texts             or not all(isinstance(t, str) and t for t in texts):
        raise TypeError('text has to be a text such as "HELLO WORLD", or a list '
                        'of texts.')
    if len(texts) > 10:
        raise ValueError("text can hold at most 10 texts.")
    for t in texts:
        unknown = sorted({ch for ch in t if ch not in codebook})
        if unknown:
            shown = ", ".join(repr(ch) for ch in unknown)
            hint = (" Write it in capital letters." if any(ch.islower()
                    for ch in unknown) else "")
            raise ValueError(f"Your CODEBOOK has no entry for {shown} in "
                             f"{t!r}.{hint}")
    return list(texts)


def _start(role, labels, sentences, team, device, settings, alphabet, codebook_id,
           texts=None):
    """Asks the server for a new run of Challenge 2, or falls back to a
    practice run with both devices on this laptop. With your own texts it
    does not ask the server at all."""
    if texts:
        print(c._paint("Practice run with your own text: it does not count.",
                       "yellow"))
        run = c._Run(role, labels, sentences, practice=True, run_id="practice")
        run.sequence = texts
        run.total = sentences + 1
        return run
    if c._server() is not None:
        try:
            payload = {
                "challenge": 2, "role": role, "led_uid": device.led.uid,
                "sensor_uid": device.sensor.uid, "master_uid": device.master_uid,
                "team": team, "symbols": len(labels), "runs": sentences,
                "codebook_id": codebook_id, "alphabet": alphabet,
                "join_id": secrets.token_urlsafe(12), **(settings or {})}
            state = c._api("POST", "/api/runs/join", payload)
            run = c._Run(role, labels, sentences, practice=False,
                         run_id=state["run_id"])
            run.total = state["total"]
            note = (c._paint("counts", "green") if state["counted"] else
                    c._paint("does NOT count (devices not registered)", "yellow"))
            print(f"Run for {c._paint(state['team'], 'bold')}: {sentences} sentences "
                  f"with {len(labels)} colours, this run {note}.")
            return run
        except (urllib.error.URLError, TimeoutError, OSError):
            pass
    if role != "both":
        raise RuntimeError(
            "The course server cannot be reached. With two laptops, the server "
            "gives both the common start, so this does not work offline. Check "
            "the WLAN, or plug both devices into one laptop for a practice run.")
    print(c._paint("The course server cannot be reached: PRACTICE RUN, it does not "
                   "count.", "yellow"))
    run = c._Run(role, labels, sentences, practice=True, run_id="practice")
    rng = random.SystemRandom()
    run.sequence = [" ".join(rng.choice(group) for group in _WORDS)
                    for _ in range(sentences)]
    run.total = sentences + 1
    return run


def _next_part(run, position, offset):
    """Says ready for this part and waits for its common start. Returns the
    phase, the start in the clock of this laptop and what the part needs."""
    if run.practice:
        receiver = c._roles["receiver"]
        if position == 0:
            return {"phase": "calibrate", "start": time.time() + _LEAD,
                    "slot": _slot(receiver.sensor.integration_time)}
        text = run.sequence[position - 1]
        return {"phase": "sentence", "start": time.time() + _LEAD,
                "sentence": position - 1, "text": text, "chars": len(text)}
    state = c._api("POST", f"/api/runs/{run.id}/ready",
                   {"role": run.role, "position": position})
    if state.get("start") is None:
        state = c._wait(run, lambda s: s["state"] != "running"
                        or s["position"] != position or s.get("start") is not None,
                        "the other laptop")
    if state["state"] != "running" or state["position"] != position:
        raise RuntimeError("The run went out of step with the server. Start "
                           "run_test again.")
    return {**state, "start": state["start"] - offset}


def _side_by_side(sending, receiving):
    """Runs the part of the sender in a second thread and the part of the
    receiver here, both at the same time; with only one of them, just that."""
    if sending is None:
        return None, receiving()
    if receiving is None:
        return sending(), None
    result, failure = {}, {}

    def send():
        try:
            result["value"] = sending()
        except BaseException as error:          # shown here, raised below
            failure["error"] = error
            print(c._paint(f"\n  send_text stopped with an error: {error!r}. "
                           f"If the receiver keeps waiting, press Ctrl+C.", "red"))

    thread = threading.Thread(target=send, daemon=True)
    thread.start()
    received = receiving()
    thread.join()
    if "error" in failure:
        raise failure["error"]
    return result.get("value"), received


def _run(run, send_text, receive_text, calibrate):
    sends = run.role in ("sender", "both")
    receives = run.role in ("receiver", "both")
    if not run.practice and run.role != "both":
        other = "receiving" if run.role == "sender" else "sending"
        c._wait(run, lambda s: s["state"] != "waiting", f"the {other} laptop")
    offset = 0.0 if run.practice else _clock_offset()
    run.received, run.durations, run.colours = [], [], []
    led = c._roles["sender"].led if sends else None

    for position in range(run.total):
        part = _next_part(run, position, offset)
        start = part["start"]

        if part["phase"] == "calibrate":
            slot = part["slot"]
            c._heading("Calibrating", "showing every colour once ")

            def show():
                for i, label in enumerate(run.labels):
                    _sleep_until(start + i * slot)
                    led.set_color(*run.rgb[label])
                    print(c._swatch(run.rgb[label]) or ".", end="", flush=True)
                _sleep_until(start + len(run.labels) * slot)
                led.off()

            def measure():
                it = c._roles["receiver"].sensor.integration_time / 1000
                readings = {}
                for i, label in enumerate(run.labels):
                    _sleep_until(start + i * slot + 2 * it + 0.25)
                    readings[label] = c._measure_calibration()
                    if not sends:
                        print(".", end="", flush=True)
                return readings

            with _Heartbeat(run):
                _, readings = _side_by_side(show if sends else None,
                                            measure if receives else None)
            print()
            if receives and calibrate is not None:
                calibrate(readings)
            _note(run, position, sent={"duration": 0, "colors": 0} if sends else None,
                  received={"text": None} if receives else None)
            continue

        index, chars = part["sentence"], part["chars"]
        text = part.get("text")
        c._heading(f"Sentence {index + 1} of {run.runs}",
                   f"{chars} characters", end="\n")
        if sends:
            print(f"  sending    {c._paint(text, 'bold')}")

        def send():
            _sleep_until(start)
            began = time.time()
            send_text(text)
            duration = time.time() - began
            led.off()
            return duration

        def receive():
            _sleep_until(start)
            return receive_text(chars)

        with _Heartbeat(run):
            duration, got = _side_by_side(send if sends else None,
                                          receive if receives else None)
        if receives:
            got = _check_text(got, chars)
            print(f"  received   {c._paint('-' if got is None else got, 'bold')}")
        sent_note = None
        if sends:
            colours = sum(len(run.codebook[ch]) for ch in text)
            sent_note = {"duration": round(duration, 4), "colors": colours}
            print(c._paint(f"  {colours} colours in {duration:.2f} s", "dim"))
        _note(run, position, sent=sent_note,
              received={"text": got} if receives else None)


def _check_text(got, chars):
    """The text receive_text returned, or None if it is no text at all."""
    if not isinstance(got, str):
        print(c._paint(f"  receive_text returned {got!r}, but it has to return the "
                       f"text it received. Counted as a mistake.", "yellow"))
        return None
    if len(got) != chars:
        print(c._paint(f"  receive_text returned {len(got)} characters, the sentence "
                       f"has {chars}.", "yellow"))
    return got


def _note(run, position, sent=None, received=None):
    """Tells the server (or, in a practice run, this module) that the part
    is done on this laptop, and waits until the other side is done too."""
    for kind, note in (("sent", sent), ("received", received)):
        if note is None:
            continue
        role = "sender" if kind == "sent" else "receiver"
        device = c._roles[role]
        device._log.write(f"word_{kind}", run=run.id, position=position, **note)
        if run.practice:
            if position > 0 and kind == "sent":
                run.durations.append(note["duration"])
                run.colours.append(note["colors"])
            if position > 0 and kind == "received":
                run.received.append(note["text"])
            continue
        c._api("POST", f"/api/runs/{run.id}/{kind}",
               {"role": run.role, "position": position, **note})
    if not run.practice:
        state = c._wait(run, lambda s: s["state"] != "running"
                        or s["position"] > position, "the other laptop")
        if state["state"] == "done":
            run.state = state


# --- The result -----------------------------------------------------------------

def _marked(sent, got):
    """The received text with every wrong character in red."""
    if got is None:
        return c._paint("-", "red")
    out = []
    for i, ch in enumerate(got):
        right = i < len(sent) and sent[i] == ch
        shown = ch if ch != " " or right else "_"
        out.append(shown if right else c._paint(shown, "red", "bold"))
    return "".join(out)


def _report(run):
    if run.practice:
        sequence, received = run.sequence, run.received
        durations, colours = run.durations, run.colours
    else:
        state = getattr(run, "state", None) or c._api(
            "GET", f"/api/runs/{run.id}?role={run.role}")
        sequence, received = state["sequence"], state["received"]
        durations, colours = state["durations"], state["colors"]
    print()
    hits = 0
    for i, (sent, got) in enumerate(zip(sequence, received)):
        right = sent == got
        hits += right
        mark = c._paint("ok", "green") if right else c._paint("MISTAKE", "red", "bold")
        print(f"  {i + 1}  sent      {sent}")
        print(f"     received  {_marked(sent, got)}   {mark}   "
              f"{durations[i]:.2f} s")
    total = sum(durations)
    chars = sum(len(s) for s in sequence)
    symbols = len(run.labels)
    rates = {}
    if total > 0:
        symbol_rate = sum(colours) / total
        rates = {"chars_per_s": round(chars / total, 2),
                 "symbols_per_s": round(symbol_rate, 2),
                 "bits_per_s": round(symbol_rate * math.log2(symbols), 2)}
    perfect = hits == len(sequence)
    kind = "Practice run" if run.practice else "Result"
    line = f"{kind}: {hits} of {len(sequence)} sentences without a mistake"
    if rates:
        line += (f", {rates['chars_per_s']:.2f} characters per second "
                 f"({rates['symbols_per_s']:.2f} colours per second, "
                 f"{rates['bits_per_s']:.2f} bit per second with {symbols} colours)")
    print(c._paint(line + ".", "bold", "green" if perfect else "red"))
    if not perfect:
        _hint(sequence, received)
    if run.practice:
        print(c._paint("This was a practice run; it does not count.", "yellow"))
    elif perfect and len(sequence) < 3:
        print(c._paint("Only runs with 3 sentences count for the challenge.", "yellow"))
    return {"hits": hits, "sentences": len(sequence), "sequence": sequence,
            "received": received, "durations": durations, **rates,
            "practice": run.practice}


def _hint(sequence, received):
    """What the mistakes suggest, as compare.py did before."""
    short = any(got is not None and len(got) < len(sent)
                for sent, got in zip(sequence, received))
    long = any(got is not None and len(got) > len(sent)
               for sent, got in zip(sequence, received))
    swapped = any(got is not None and len(got) == len(sent) and got != sent
                  for sent, got in zip(sequence, received))
    if short or long:
        print(c._paint("Characters went missing or appeared twice: sender and "
                       "receiver were probably out of step. That points to timing.",
                       "yellow"))
    if swapped:
        print(c._paint("Single characters came out wrong: colours were mixed up. "
                       "Try a slower SYMBOL_RATE, or look at the calibration.",
                       "yellow"))
```
