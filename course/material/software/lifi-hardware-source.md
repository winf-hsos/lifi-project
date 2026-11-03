# Source of `lifi_hardware` 0.5.0

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

__version__ = "0.5.0"

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

    COLORS = [(0, 0, 0), (255, 255, 255)]

    def calibrate(readings):
        ...                                   # learn what each symbol looks like

    def send_symbol(index):
        sender.led.set_color(*COLORS[index])

    def receive_symbol():
        r, g, b, c = receiver.sensor.read()
        ...                                   # which symbol was it?
        return 0

    run_test(send_symbol, receive_symbol, calibrate, symbols=len(COLORS))

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
import time
import urllib.error
import urllib.request
from typing import cast

from . import LifiDevice, find_devices
from ._telemetry import DEFAULT_SERVER

_READINGS_PER_SYMBOL = 5     # readings per symbol during calibration
_POLL = 0.15                 # seconds between two questions to the server
_WAIT_FOR_PARTNER = 300      # seconds to wait for the other laptop
_TIMEOUT = 5                 # seconds for one request to the server


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
    print(f"Sender: {sending}, receiver: {receiving}")
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


def _api(method, path, body=None):
    request = urllib.request.Request(
        _server() + path, method=method,
        data=None if body is None else json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=_TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        try:
            detail = json.loads(error.read().decode("utf-8")).get("detail")
        except (ValueError, AttributeError):
            detail = None
        raise ServerError(detail or f"the server answered {error.code}") from None


# --- Noting what was sent and received ------------------------------------------

class _Run:
    """One run of run_test: on the server, or locally as a practice run."""

    def __init__(self, role, symbols, runs, practice, run_id=None):
        self.role = role
        self.symbols = symbols
        self.runs = runs
        self.practice = practice
        self.id = run_id
        self.sequence = None         # known locally only in a practice run
        self.received = []


def note_sent(run, position, symbol):
    """Notes that ``symbol`` now shows at ``position`` of the run.

    Called by run_test only, never by your own code: what counts as sent
    is decided by the test, not by the program being tested. The note goes
    into the measurement log of the sending device and to the server.
    """
    device = _roles["sender"]
    device._log.write("note_sent", run=run.id, position=position, symbol=symbol)
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
                      symbol=symbol)
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


def _check(symbol, symbols):
    if isinstance(symbol, bool) or not isinstance(symbol, int) or not 0 <= symbol < symbols:
        print(f"  receive_symbol() returned {symbol!r}, but it has to return a "
              f"whole number from 0 to {symbols - 1}. Counted as a mistake.")
        return None
    return symbol


def _wait(run, until, what):
    """Asks the server until ``until(state)`` holds and returns that state."""
    started = time.time()
    shown = False
    while True:
        state = _api("GET", f"/api/runs/{run.id}?role={run.role}")
        if until(state):
            return state
        if not shown and time.time() - started > 2:
            print(f"  waiting for {what} ...")
            shown = True
        if time.time() - started > _WAIT_FOR_PARTNER:
            raise RuntimeError(f"Waited {_WAIT_FOR_PARTNER} s for {what}. "
                               f"Start run_test again on both laptops.")
        time.sleep(_POLL)


def run_test(send_symbol, receive_symbol, calibrate=None, symbols=None,
             runs=20, team=None):
    """The test for Challenge 1: how many symbols get through without a mistake?

    ``send_symbol(index)`` shows the symbol with that number, from 0 to
    ``symbols - 1``. ``receive_symbol()`` measures and returns the number of
    the symbol it recognised. ``calibrate(readings)`` is called once before
    the test, after the whole alphabet has been shown once: ``readings`` is a
    dictionary from each symbol number to a list of Readings taken while that
    symbol was showing. What you make of them is up to you.

    ``symbols`` is the size of your alphabet, usually ``len(COLORS)``. ``team``
    is needed only if your devices are not registered with a team yet: then
    both laptops find each other by this name, and the run does not count.

    Returns a dictionary with the number of hits and the two sequences.
    """
    if symbols is None:
        raise TypeError("run_test needs the size of your alphabet, for "
                        "example run_test(..., symbols=len(COLORS))")
    roles = _choose_roles()
    role = ("both" if roles["sender"] and roles["receiver"]
            else "sender" if roles["sender"] else "receiver")
    some_device = roles["sender"] or roles["receiver"]

    run = _start(role, symbols, runs, team, some_device)
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
    return _report(run)


def _start(role, symbols, runs, team, device):
    """Asks the server for a new run, or falls back to a practice run."""
    if _server() is not None:
        try:
            state = _api("POST", "/api/runs/join", {
                "role": role, "led_uid": device.led.uid,
                "sensor_uid": device.sensor.uid, "team": team,
                "symbols": symbols, "runs": runs})
            run = _Run(role, symbols, runs, practice=False, run_id=state["run_id"])
            note = "counts" if state["counted"] else "does NOT count (devices not registered)"
            print(f"Run for {state['team']}: {symbols} symbols, {runs} runs, this run {note}.")
            return run
        except (urllib.error.URLError, TimeoutError, OSError):
            pass
    if role != "both":
        raise RuntimeError(
            "The course server cannot be reached. With two laptops, the server "
            "keeps the two in step, so this does not work offline. Check the "
            "WLAN, or plug both devices into one laptop for a practice run.")
    print("The course server cannot be reached: PRACTICE RUN, it does not count.")
    run = _Run(role, symbols, runs, practice=True, run_id="practice")
    rng = random.SystemRandom()
    run.sequence = [rng.randrange(symbols) for _ in range(runs)]
    return run


def _steps(run):
    """The steps of a practice run, in the same order as on the server."""
    return ([("calibrate", i) for i in range(run.symbols)]
            + [("test", s) for s in run.sequence])


def _run_both(run, send_symbol, receive_symbol, calibrate):
    """Both devices on this laptop: send, wait, measure, note, next."""
    print("Calibrating: showing the whole alphabet once ...")
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
            if calibrate is not None:
                calibrate(readings)
            print(f"Testing {run.runs} symbols ...")
        send_symbol(symbol)
        time.sleep(_settle_time())
        note_sent(run, position, symbol)
        if phase == "calibrate":
            readings[symbol] = _measure_calibration()
            note_received(run, position, None)
        else:
            got = _check(receive_symbol(), run.symbols)
            run.received.append(got)
            note_received(run, position, got)
            mark = "ok" if got == symbol else "MISTAKE"
            print(f"  {position - run.symbols + 1:>3}/{run.runs}  sent {symbol}  "
                  f"recognised {got}  {mark}")
        position += 1


def _run_sender(run, send_symbol):
    """This laptop only sends; the server says what and when."""
    _wait(run, lambda s: s["state"] != "waiting", "the receiving laptop")
    print("Calibrating: showing the whole alphabet once ...")
    while True:
        state = _wait(run, lambda s: s["state"] == "done" or not s["sent"],
                      "the receiver")
        if state["state"] == "done":
            run.state = state
            return
        position, symbol = state["position"], state["symbol"]
        if state["phase"] == "test" and position == run.symbols:
            print(f"Testing {run.runs} symbols ...")
        send_symbol(symbol)
        time.sleep(0.1)
        note_sent(run, position, symbol)
        if state["phase"] == "test":
            print(f"  {position - run.symbols + 1:>3}/{run.runs}  sent {symbol}")
        # Wait until the receiver has measured, then the next symbol comes
        _wait(run, lambda s: s["state"] == "done" or s["position"] > position,
              "the receiver")


def _run_receiver(run, receive_symbol, calibrate):
    """This laptop only receives; it measures whenever the sender is ready."""
    _wait(run, lambda s: s["state"] != "waiting", "the sending laptop")
    print("Calibrating: measuring the whole alphabet once ...")
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
            readings[state["symbol"]] = _measure_calibration()
            note_received(run, position, None)
            continue
        if position == run.symbols:
            if calibrate is not None:
                calibrate(readings)
            print(f"Testing {run.runs} symbols ...")
        got = _check(receive_symbol(), run.symbols)
        run.received.append(got)
        result = note_received(run, position, got)
        print(f"  {position - run.symbols + 1:>3}/{run.runs}  recognised {got}")
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
    kind = "Practice run" if run.practice else "Result"
    print(f"{kind}: {hits} of {run.runs} recognised with {run.symbols} symbols.")
    mistakes = [(i + 1, a, b) for i, (a, b) in enumerate(zip(sequence, received))
                if a != b]
    if mistakes:
        print("Mistakes (position: sent -> recognised):")
        for position, sent, got in mistakes:
            print(f"  {position:>3}: {sent} -> {got}")
        pairs = {}
        for _, sent, got in mistakes:
            pairs[(sent, got)] = pairs.get((sent, got), 0) + 1
        common = max(pairs.items(), key=lambda item: item[1])
        if common[1] > 1:
            (sent, got), count = common
            print(f"{sent} was taken for {got} {count} times: these two are "
                  f"probably too close together.")
    else:
        print("No mistakes.")
    return {"hits": hits, "runs": run.runs, "symbols": run.symbols,
            "sequence": sequence, "received": received,
            "practice": run.practice}
```
