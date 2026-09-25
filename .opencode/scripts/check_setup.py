"""Check that your laptop is ready for the LiFi Project.

Run by the /onboarding command in OpenCode, or by hand:

    python .opencode/scripts/check_setup.py             check everything
    python .opencode/scripts/check_setup.py --install   also install lifi_hardware if missing

(on a Mac: python3)

Every check prints one line starting with OK, FAIL or SKIP, followed by what
was found and, for a FAIL, what to do. The LED test switches your LED green
for three seconds: look at the device while it runs.
"""

import os
import platform
import shutil
import socket
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODULE_URL = "https://github.com/winf-hsos/lifi-hardware/archive/refs/heads/main.zip"
COURSE_SERVER = "https://lifi.uber.space"
results = []


def report(status, name, detail, advice=""):
    results.append(status)
    line = f"{status:<4}  {name}: {detail}"
    if advice and status == "FAIL":
        line += f"\n      -> {advice}"
    print(line, flush=True)


def check_system():
    name = {"Windows": "Windows", "Darwin": "macOS"}.get(platform.system(), platform.system())
    version = platform.mac_ver()[0] if name == "macOS" else platform.release()
    report("OK", "Operating system", f"{name} {version}".strip())


def brickd_usb_trouble():
    """True if the Brick Daemon log shows a USB device it could not take over.

    Seen on Windows: right after plugging in, the daemon cannot read the
    device's name (LIBUSB_ERROR_PIPE) and then ignores the device until it
    is plugged in again. The log only exists on Windows and Linux."""
    candidates = [r"C:\ProgramData\Tinkerforge\Brickd\brickd.log",
                  "/var/log/brickd.log"]
    for path in candidates:
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                tail = f.readlines()[-40:]
        except OSError:
            continue
        last_problem = max((i for i, line in enumerate(tail)
                            if "could not be acquired correctly" in line), default=-1)
        last_added = max((i for i, line in enumerate(tail)
                          if "Added USB device" in line),
                         default=-1)
        return last_problem > last_added
    return False


def check_python():
    v = sys.version_info
    text = f"Python {v.major}.{v.minor}.{v.micro} at {sys.executable}"
    if (v.major, v.minor) >= (3, 10):
        report("OK", "Python", text)
        return True
    report("FAIL", "Python", text + " is too old",
           "Install a current Python from python.org (see the installation page, or ask your assistant).")
    return False


def check_git():
    """Only for folders cloned with Git; a ZIP folder does not need Git."""
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        return
    if shutil.which("git"):
        out = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
        report("OK", "Git", out + " (your course folder is a Git clone)")
    else:
        report("FAIL", "Git", "your course folder is a Git clone, but Git is not found",
               "Install Git again (see the installation page), then restart OpenCode.")


def check_module(install):
    try:
        import lifi_hardware  # noqa: F401
    except ImportError:
        if not install:
            report("FAIL", "lifi_hardware", "not installed",
                   "Run this check again with --install, or see the installation page.")
            return False
        print("      installing lifi_hardware, this can take a minute ...", flush=True)
        result = subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", MODULE_URL],
                                capture_output=True, text=True, errors="replace")
        if result.returncode != 0:
            report("FAIL", "lifi_hardware", "installation failed: " + result.stderr.strip()[-600:],
                   "Show this message to your assistant.")
            return False
        try:
            import importlib
            importlib.invalidate_caches()
            import lifi_hardware  # noqa: F401,F811
        except ImportError as error:
            report("FAIL", "lifi_hardware", f"installed but cannot be imported: {error}",
                   "Close and reopen the terminal, then run the check again.")
            return False
    from lifi_hardware import __version__
    report("OK", "lifi_hardware", f"version {__version__}")
    return True


def check_daemon():
    try:
        with socket.create_connection(("localhost", 4223), timeout=2):
            report("OK", "Brick Daemon", "running and reachable on localhost:4223")
            return True
    except OSError:
        report("FAIL", "Brick Daemon", "not reachable on localhost:4223",
               "Install the Brick Daemon (see the installation page, or ask your assistant), or start it again; on Windows it is "
               "a service, on macOS restart the laptop once after installing.")
        return False


def check_server():
    """Is the course server reachable? Not having it is no error: everything works offline."""
    import urllib.request
    try:
        with urllib.request.urlopen(COURSE_SERVER + "/api/health", timeout=5) as r:
            ok = r.status == 200
    except Exception:
        ok = False
    if ok:
        report("OK", "Course server", "reachable; your device announces itself there during the test")
    else:
        report("SKIP", "Course server", "not reachable right now (no internet?). Everything works "
               "without it; your device will announce itself the next time you are online")
    return ok


def check_device():
    from lifi_hardware import LifiDevice
    try:
        # With the upload switched on (unless LIFI_SERVER=off), so that the device
        # announces itself to the course server and can be assigned to a team.
        lifi = LifiDevice.connect(log_file=None)
    except Exception as error:  # the module explains what is missing
        if brickd_usb_trouble():
            advice = ("The Brick Daemon saw your device but could not take it over, a known "
                      "USB hiccup. Unplug the USB cable, wait five seconds, plug it in again, "
                      "then run the check again.")
        else:
            advice = ("Plug the device in with a data cable (some cables only charge), check "
                      "it in the Brick Viewer, then run the check again.")
        report("FAIL", "Device", str(error), advice)
        return
    try:
        report("OK", "Device", f"LED {lifi.led.uid}, colour sensor {lifi.sensor.uid} "
                               "(note these two IDs: Nicolas uses them to assign your device to your team)")
        lifi.led.set_color(0, 255, 0)
        print("      the LED should now shine GREEN for three seconds ...", flush=True)
        time.sleep(3)
        lifi.led.off()
        report("OK", "LED", "set to green and back off (did you see it?)")
        readings = []
        for _ in range(3):
            readings.append(lifi.sensor.read())
            time.sleep(0.8)   # longer than the longest integration time, so each reading is new
        text = "; ".join(f"r={r.r} g={r.g} b={r.b} c={r.c}" for r in readings)
        report("OK", "Colour sensor", f"three readings: {text}")
    except Exception as error:
        report("FAIL", "Device test", str(error), "Show this message to your assistant.")
    finally:
        lifi.close()


def main():
    install = "--install" in sys.argv
    print("Checking your setup for the LiFi Project ...\n", flush=True)
    check_system()
    python_ok = check_python()
    check_git()
    module_ok = python_ok and check_module(install)
    if not python_ok:
        report("SKIP", "lifi_hardware", "needs a current Python first")
    daemon_ok = check_daemon()
    if module_ok and daemon_ok:
        check_server()
        check_device()
    else:
        report("SKIP", "Device", "needs lifi_hardware and the Brick Daemon first")

    failed = results.count("FAIL")
    print()
    if failed == 0 and "SKIP" not in results:
        print("SUMMARY: everything works. You are ready for Challenge 0.")
    else:
        print(f"SUMMARY: {failed} problem(s). Fix them from the top, then run the check again.")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
