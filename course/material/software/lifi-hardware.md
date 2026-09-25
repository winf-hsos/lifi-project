# The module `lifi_hardware`

Online: <https://docs.lifi-project.de/software/lifi-hardware.html>

In Python, a module is a piece of finished program code that you pull into your own program with a single `import` line and then use. Practically every Python program works this way: for maths, random numbers or timing nobody writes the code themselves, they import the module that does it. The word has nothing to do with the "module" in your study programme, by the way. It is unfortunately used for both.

`lifi_hardware` is such a Python module. I wrote it for this course. It holds the code that talks to your LiFi device, and you work with it for the whole project.

The hardware itself comes from Tinkerforge, and Tinkerforge ships its own programming interface. You could work with that directly. You will not, at least not at the start, and here is why.

## Why the module exists

This is what a program looks like that sets a colour and fetches one reading through the Tinkerforge interface:

```python
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_v2 import BrickletRGBLEDV2
from tinkerforge.bricklet_color_v2 import BrickletColorV2

HOST = "localhost"
PORT = 4223
UID_LED = "ABC"       # printed on the part, or shown in the Brick Viewer
UID_SENSOR = "XYZ"

ipcon = IPConnection()
led = BrickletRGBLEDV2(UID_LED, ipcon)
sensor = BrickletColorV2(UID_SENSOR, ipcon)
ipcon.connect(HOST, PORT)

led.set_rgb_value(255, 0, 0)
r, g, b, c = sensor.get_color()
print(r, g, b, c)

ipcon.disconnect()
```

The same with the module:

```python
from lifi_hardware import led, sensor

led.set_color(255, 0, 0)
print(sensor.read())
```

The difference is not just a few lines. The upper version contains at least five things you cannot possibly understand in your first days: what an IP connection is, why a program on your own laptop needs a network address, what a port is, what a UID is and where you get one, and why you have to disconnect at the end.

None of that is the subject of this course. It would be ballast you carry along without learning anything from it. The module takes that part off your hands and leaves exactly what this is actually about: making light, measuring light, and the two settings with which you influence the measurement.

## What the module does not take off your hands

It does not hide everything, and that is deliberate. The two settings of the sensor stay visible, because the most important trade-off of the project hangs on them. Whoever never sees them cannot tune their throughput.

## Installing and updating

You do not have to do anything yourself: `/onboarding` installs the module in your first session, and `/update-semester` installs a new version whenever the course needs one, for instance when a function is added or a bug is fixed.

By hand, it is one command in a terminal (on a Mac `pip3` if `pip` is not found):

```bash
pip install https://github.com/winf-hsos/lifi-hardware/archive/refs/heads/main.zip
```

The Tinkerforge library comes along automatically as a dependency. The code itself lives in a public GitHub repository: [github.com/winf-hsos/lifi-hardware](https://github.com/winf-hsos/lifi-hardware).

## The interface

To begin with, one line that brings in two objects is enough:

```python
from lifi_hardware import led, sensor
```

Both connect to your device by themselves the first time you use them. You need no addresses, no identifiers, no configuration. When your program ends, the LED goes off automatically and the connection is closed cleanly.

### The LED (the sender)

```python
led.set_color(r, g, b)   # each value 0 to 255
led.off()                # the same as led.set_color(0, 0, 0)
led.color                # the current colour as (r, g, b), read from the hardware
```

The hardware keeps a colour you have set until another command arrives. It knows nothing about your program. If you use `led` and `sensor` as shown above, the module switches the LED off for you when your program ends, and that includes an end by Ctrl+C or by an error. If you take the `LifiDevice` route described further down, the LED stays on unless you close the device yourself. `led.color` asks the hardware itself, not a remembered value. That helps when you are hunting a fault and want to know what is really shining right now.

### The sensor (the receiver)

```python
reading = sensor.read()          # Reading(r, g, b, c), each value 0 to 65535
r, g, b, c = sensor.read()       # unpacks straight into four variables

sensor.set_integration_time(ms)  # allowed: 2.4, 24, 101, 154 or 700
sensor.set_gain(factor)          # allowed: 1, 4, 16 or 60
sensor.integration_time          # look up the current setting
sensor.gain                      # look up the current setting
sensor.set_light(True)           # the sensor's white illumination LED
```

Four things you have to know about the sensor.

First, it measures four channels, not three. Red, green and blue are filtered; the fourth channel `c`, the clear channel, measures unfiltered and is therefore the most sensitive.

Second, the readings do not correspond to the RGB values you sent. In between lie overlapping filters, the distance and the ambient light, and that is exactly why you calibrate.

Third, the sensor measures at its own pace, one measurement per integration time. `read()` fetches the most recent finished measurement and does not wait. If you read more often than the sensor measures, you get the same value several times; new information arrives at most once per integration time. That is precisely why the integration time is a setting: calmer values against fewer measurements per second.

Fourth, the sensor always starts in a known state: gain 16, integration time 154 ms, illumination LED off, so that measurement series are comparable. Which settings suit your link, only your own measurements can tell you.

The small white illumination LED on the sensor, by the way, is meant for lighting objects whose surface colour you want to measure. For your light link it only gets in the way, so it is off at the start, and you leave it off.

### More control when you need it

If you want to decide yourself when to connect and disconnect, take the class behind the two convenient objects:

```python
from lifi_hardware import LifiDevice

lifi = LifiDevice.connect()      # finds LED and sensor by itself
lifi.led.set_color(255, 0, 0)
print(lifi.sensor.read())
lifi.close()                     # LED off, connection closed
```

The same with the clean-up built in: the `with` form closes the device for you at the end of the block, even if your code inside it fails.

```python
with LifiDevice.connect() as lifi:
    lifi.led.set_color(255, 0, 0)
    print(lifi.sensor.read())
```

`connect()` also knows a few options, for example `log_file=None` (no measurement log) and `server=None` (no upload, more on that in a moment).

## The measurement log and the cockpit

Everything your device does, the module writes to a file called `lifi_log.jsonl` in the folder your program runs in: every colour you set, every reading, every change of a setting, one plain-text line per event. This is the memory of your measurement series. It belongs to you, and it always works, even without any internet.

In addition, the module sends the same events to the course server. That lets you see your own link live in the browser, in the [team cockpit](https://lifi.uber.space/cockpit): at the top what your LED sends, below it what your sensor measures, on a shared time axis. When the two do not fit together, you are looking at your fault. The cockpit is your most important tool for finding faults on the link. How to work with it is on its own page, [The team cockpit](cockpit.md).

Full transparency applies. What is uploaded is exactly what is in your local file, not a line more. If your program crashes, the type of error goes along too, with a cleaned message (file paths are removed beforehand, and your source code never goes along); the error then appears as a red mark in your cockpit. If you do not want the upload, you switch it off at any time and without any disadvantage, with `LifiDevice.connect(server=None)` or the environment variable `LIFI_SERVER=off`. The local log keeps running regardless.

## Look inside

The module is not a magic trick. It is a manageable amount of Python code that you can open and read, and from Challenge 2 at the latest you should do that once. The source lies open in its [GitHub repository](https://github.com/winf-hsos/lifi-hardware), and your assistant has a copy of it too. In it you will find the same Tinkerforge calls as in the first example above, plus a few lines that look up your device's identifiers by themselves, so that you never have to type a UID.

This is a pattern you will meet constantly in your studies: under every convenient interface lies a less convenient one, and under that another. The Tinkerforge interface in turn hides how the data actually travels over the USB cable. And below that it goes on, down to single voltage levels on a wire.

If you ever need something the module cannot do, you may reach one level down at any time and use the Tinkerforge interface directly. The module leaves the door open on purpose: `led.raw` and `sensor.raw` are the Tinkerforge objects underneath, with everything they can do. It is not forbidden. You just do not have to do it on the first day.
