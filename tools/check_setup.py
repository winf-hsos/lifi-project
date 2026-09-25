"""Check that your laptop is ready for the LiFi Project.

Run by the /onboarding command in OpenCode, or by hand:

    python tools/check_setup.py             check everything
    python tools/check_setup.py --install   also install lifi_hardware if missing

(on a Mac: python3)

Every check prints one line starting with OK, FAIL or SKIP, followed by what
was found and, for a FAIL, what to do. The LED test switches your LED green
for three seconds: look at the device while it runs.
"""

import os
import shutil
import socket
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE_URL = "git+https://github.com/winf-hsos/lifi-hardware.git"
results = []


def report(status, name, detail, advice=""):
    results.append(status)
    line = f"{status:<4}  {name}: {detail}"
    if advice and status == "FAIL":
        line += f"\n      -> {advice}"
    print(line, flush=True)


def check_python():
    v = sys.version_info
    text = f"Python {v.major}.{v.minor}.{v.micro} at {sys.executable}"
    if (v.major, v.minor) >= (3, 10):
        report("OK", "Python", text)
        return True
    report("FAIL", "Python", text + " is too old",
           "Install a current Python from python.org (step 1 of the installation page).")
    return False


def check_git():
    if shutil.which("git"):
        out = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
        report("OK", "Git", out)
    else:
        report("FAIL", "Git", "not found",
               "Install Git (step 2 of the installation page), then restart VS Code.")


def check_key():
    path = os.path.join(ROOT, "openai.key")
    if not os.path.isfile(path):
        report("FAIL", "Key file", "openai.key not found in the course folder",
               "Create the file openai.key next to AGENTS.md and paste your key into it.")
        return
    with open(path, encoding="utf-8", errors="replace") as f:
        key = f.read().strip()
    if key.startswith("sk-") and len(key) > 20 and "\n" not in key:
        report("OK", "Key file", "openai.key is there and looks like a key (not shown)")
    else:
        report("FAIL", "Key file", "openai.key does not look like a key",
               "Open the file: it must contain only your key, one line starting with sk-.")


def check_module(install):
    try:
        import lifi_hardware  # noqa: F401
    except ImportError:
        if not install:
            report("FAIL", "lifi_hardware", "not installed",
                   "Run this check again with --install, or see step 7 of the installation page.")
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
               "Install the Brick Daemon (step 6), or start it again; on Windows it is "
               "a service, on macOS restart the laptop once after installing.")
        return False


def check_device():
    from lifi_hardware import LifiDevice
    try:
        lifi = LifiDevice.connect(log_file=None, server=None)
    except Exception as error:  # the module explains what is missing
        report("FAIL", "Device", str(error),
               "Plug the device in with a data cable, check it in the Brick Viewer, "
               "then run the check again.")
        return
    try:
        report("OK", "Device", f"LED {lifi.led.uid}, colour sensor {lifi.sensor.uid} "
                               "(note these two IDs, you will need them)")
        lifi.led.set_color(0, 255, 0)
        print("      the LED should now shine GREEN for three seconds ...", flush=True)
        time.sleep(3)
        lifi.led.off()
        report("OK", "LED", "set to green and back off (did you see it?)")
        readings = [lifi.sensor.read() for _ in range(3)]
        text = "; ".join(f"r={r.r} g={r.g} b={r.b} c={r.c}" for r in readings)
        report("OK", "Colour sensor", f"three readings: {text}")
    except Exception as error:
        report("FAIL", "Device test", str(error), "Show this message to your assistant.")
    finally:
        lifi.close()


def main():
    install = "--install" in sys.argv
    print("Checking your setup for the LiFi Project ...\n", flush=True)
    python_ok = check_python()
    check_git()
    check_key()
    module_ok = python_ok and check_module(install)
    if not python_ok:
        report("SKIP", "lifi_hardware", "needs a current Python first")
    daemon_ok = check_daemon()
    if module_ok and daemon_ok:
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
