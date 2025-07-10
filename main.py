#!/bin/env python3

import argparse, secrets

VERSION = "1.5.0"


def apply_color(chars: str) -> str:
    colors = {
        "lower": "92",
        "upper": "93",
        "digit": "94",
        "other": "95",
    }

    result = []

    for char in chars:
        if char.islower():
            char = "\033[{}m{}\033[00m".format(colors["lower"], char)
        elif char.isupper():
            char = "\033[{}m{}\033[00m".format(colors["upper"], char)
        elif char.isdigit():
            char = "\033[{}m{}\033[00m".format(colors["digit"], char)
        else:
            char = "\033[{}m{}\033[00m".format(colors["other"], char)

        result.append(char)

    return "".join(result)


# Check if generated password contains characters from every group
def is_strong(result: str, nosymbols: bool) -> bool:
    sets: list[int] = [0, 0, 0, 1 if nosymbols else 0]

    for char in result:
        if char.islower():
            sets[0] = 1
        elif char.isupper():
            sets[1] = 1
        elif char.isdigit():
            sets[2] = 1
        else:
            sets[3] = 1

    return sets == [1, 1, 1, 1]


def genpwd(length: int = 32, nosymbols: bool = False, nocolor: bool = False) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    if not nosymbols:
        # No quote ["'`] characters
        chars = chars + "!#$%&()*+,-.:;<=>?@^_/\\|[]{}~"

    length = min(max(16, length), 128)

    while True:
        result = "".join([secrets.choice(chars) for _ in range(length)])

        if is_strong(result, nosymbols):
            break

    if nocolor:
        return result
    else:
        return apply_color(result)


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        prog="genpwd", description="Generate very strong passwords"
    )
    arg_parser.add_argument(
        "-C", "--nocolor", action="store_true", help="print passwords in no color"
    )
    arg_parser.add_argument(
        "-S",
        "--nosymbols",
        action="store_true",
        help="exclude special symbol characters",
    )
    arg_parser.add_argument(
        "-l",
        "--length",
        action="store",
        type=int,
        default=32,
        help="password length (from 16 to 128)",
    )
    arg_parser.add_argument(
        "-n",
        "--count",
        action="store",
        type=int,
        default=1,
        help="numbers of passwords to generate (from 1 to 20)",
    )
    arg_parser.add_argument(
        "-v", "--version", action="store_true", help="print version number and exit"
    )
    args = arg_parser.parse_args()

    if args.version:
        return print(VERSION)

    count = min(max(1, args.count), 20)

    for _ in range(count):
        print(genpwd(args.length, args.nosymbols, args.nocolor))


if __name__ == "__main__":
    main()
