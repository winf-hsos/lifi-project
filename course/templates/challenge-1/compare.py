"""
Compares the logs of both sides and prints the result.

You do not change this script.

    python compare.py

Expects `sent.txt` and `received.txt` in the same folder.
"""

import sys


def read_log(filename):
    header = {}
    symbols = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                header[key] = value
            elif line:
                symbols.append(int(line))
    return header, symbols


def main():
    try:
        sent_header, sent = read_log("sent.txt")
        received_header, received = read_log("received.txt")
    except FileNotFoundError as error:
        print(f"Missing: {error.filename}")
        print("Both log files have to be in this folder.")
        sys.exit(1)

    alphabet_size = int(sent_header["alphabet_size"])
    team = sent_header.get("team", "unknown")

    if len(sent) != len(received):
        print("Warning: the logs contain different numbers of symbols.")
        print(f"  sent: {len(sent)}, received: {len(received)}")
        print("The receiver has probably lost the beat.")

    pairs = list(zip(sent, received))
    errors = [(position, a, b) for position, (a, b) in enumerate(pairs) if a != b]
    passed = len(errors) == 0 and len(sent) == len(received)

    print()
    print(f"Team {team} · Challenge 1")
    print(f"Alphabet size:   {alphabet_size:>5}")
    print(f"Bits per symbol: {alphabet_size.bit_length() - 1:>5}")
    print(f"Runs:            {len(pairs):>5}")
    print(f"Errors:          {len(errors):>5}")
    print(f"Sender duration: {float(sent_header['duration']):>5.1f} s")
    print()

    if passed:
        print(f"Result: passed, {alphabet_size} symbols counted")
    else:
        print("Result: not passed for this alphabet size")
        print()
        print("The first mix-ups:")
        for position, expected, actual in errors[:10]:
            print(f"  position {position + 1}: sent {expected}, recognised {actual}")
        print()
        print("Tip: if the same two symbols are mixed up every time, they are too")
        print("close together. If it looks random, the timing or the calibration")
        print("is the more likely culprit.")


if __name__ == "__main__":
    main()
