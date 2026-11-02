"""
Test script for Challenge 1.

You do not change this script. At the acceptance test the original version runs.

How it works: start it twice, once as sender and once as receiver, on two
computers or in two terminals on the same one. The sender runs your
sender.py, the receiver your receiver.py. Both sides write a log. Afterwards
`compare.py` compares the two logs and prints the result.

    python run_test.py sender
    python run_test.py receiver

Optionally change the number of runs (default 50):

    python run_test.py sender --runs 10
"""

import argparse
import random
import time

import agreement

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
    return [generator.randrange(agreement.ALPHABET_SIZE) for _ in range(runs)]


def wait_for_start(role):
    print()
    print(f"Role: {role}")
    print(f"Alphabet size according to agreement.py: {agreement.ALPHABET_SIZE}")
    print()
    input("Both sides ready? Then press Enter on both sides at the same time. ")


def run_sender(arguments):
    import sender      # only the sending side, so the receiver's device stays untouched

    sequence = build_sequence(arguments.runs)

    wait_for_start("sender")

    print("Calibrating ...")
    sender.calibrate()

    print(f"Transmitting {arguments.runs} symbols ...")
    started = time.time()
    for position, symbol in enumerate(sequence):
        sender.send_symbol(symbol)
        print(f"  {position + 1}/{arguments.runs}  sent: {symbol}")
    duration = time.time() - started

    write_log("sent.txt", arguments, sequence, duration)


def run_receiver(arguments):
    import receiver    # only the receiving side

    wait_for_start("receiver")

    print("Calibrating ...")
    receiver.calibrate()

    print(f"Receiving {arguments.runs} symbols ...")
    received = []
    started = time.time()
    for position in range(arguments.runs):
        symbol = receiver.receive_symbol()
        received.append(symbol)
        print(f"  {position + 1}/{arguments.runs}  recognised: {symbol}")
    duration = time.time() - started

    write_log("received.txt", arguments, received, duration)


def write_log(filename, arguments, symbols, duration):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"team={arguments.team}\n")
        file.write(f"alphabet_size={agreement.ALPHABET_SIZE}\n")
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
