"""
Test script for Challenge 1.

You do not change this script. At the acceptance test the original version runs.

How it works: start it on both computers, one as sender, one as receiver.
Both sides write a log. Afterwards `compare.py` compares the two logs and
prints the result.

    python run_test.py sender
    python run_test.py receiver

Optionally change the number of runs (default 50):

    python run_test.py sender --runs 10
"""

import argparse
import random
import time

import device

SEED = 20260817          # fixed random sequence so that both sides expect the same
DEFAULT_RUNS = 50


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("role", choices=["sender", "receiver"])
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--team", default="unknown")
    return parser.parse_args()


def build_sequence(runs):
    """Creates the sequence of symbols to send. The same on both sides."""
    generator = random.Random(SEED)
    return [generator.randrange(device.ALPHABET_SIZE) for _ in range(runs)]


def wait_for_start(role):
    print()
    print(f"Role: {role}")
    print(f"Alphabet size according to your code: {device.ALPHABET_SIZE}")
    print()
    input("Both sides ready? Then press Enter on both computers at the same time. ")


def run_sender(arguments):
    sequence = build_sequence(arguments.runs)

    wait_for_start("sender")

    print("Calibrating ...")
    device.calibrate_sender()

    print(f"Transmitting {arguments.runs} symbols ...")
    started = time.time()
    for position, symbol in enumerate(sequence):
        device.send_symbol(symbol)
        print(f"  {position + 1}/{arguments.runs}  sent: {symbol}")
    duration = time.time() - started

    write_log("sent.txt", arguments, sequence, duration)


def run_receiver(arguments):
    wait_for_start("receiver")

    print("Calibrating ...")
    device.calibrate_receiver()

    print(f"Receiving {arguments.runs} symbols ...")
    received = []
    started = time.time()
    for position in range(arguments.runs):
        symbol = device.receive_symbol()
        received.append(symbol)
        print(f"  {position + 1}/{arguments.runs}  recognised: {symbol}")
    duration = time.time() - started

    write_log("received.txt", arguments, received, duration)


def write_log(filename, arguments, symbols, duration):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"team={arguments.team}\n")
        file.write(f"alphabet_size={device.ALPHABET_SIZE}\n")
        file.write(f"runs={arguments.runs}\n")
        file.write(f"duration={duration:.2f}\n")
        for symbol in symbols:
            file.write(f"{symbol}\n")

    print()
    print(f"Log written: {filename}")
    print("Bring both log files onto one computer and run this there:")
    print("    python compare.py")


def main():
    arguments = parse_arguments()
    if arguments.role == "sender":
        run_sender(arguments)
    else:
        run_receiver(arguments)


if __name__ == "__main__":
    main()
