#!/bin/env python3

import argparse, secrets

VERSION = "1.5.0"

CHARACTERS = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digit": "0123456789",
    "symbol": "!#$%&()*+,-.:;<=>?@^_/|[]{}~",  # Excluded "'`\
    "extended": "".join(
        [chr(cp) for cp in range(0xC0, 0xFF + 1)]
    ),  # Latin-1 Supplement
}


def apply_color(chars: str) -> str:
    colors = {
        "lower": "92",
        "upper": "93",
        "digit": "94",
        "symbol": "95",
        "extended": "91",
    }

    result: list[str] = []

    for char in chars:
        if char in CHARACTERS["lower"]:
            char = "\033[{}m{}\033[00m".format(colors["lower"], char)
        elif char in CHARACTERS["upper"]:
            char = "\033[{}m{}\033[00m".format(colors["upper"], char)
        elif char in CHARACTERS["digit"]:
            char = "\033[{}m{}\033[00m".format(colors["digit"], char)
        elif char in CHARACTERS["symbol"]:
            char = "\033[{}m{}\033[00m".format(colors["symbol"], char)
        elif char in CHARACTERS["extended"]:
            char = "\033[{}m{}\033[00m".format(colors["extended"], char)

        result.append(char)

    return "".join(result)


# Check if generated password contains characters from every group
def is_strong(
    result: str, nosymbols: bool, extended: bool, length: int, atleast: int
) -> bool:
    included_chars = {
        "lower": 0,
        "upper": 0,
        "digit": 0,
        "symbol": 0,
        "extended": 0,
    }

    if len(result) < length:
        return False

    for char in result:
        if char in CHARACTERS["lower"]:
            included_chars["lower"] = included_chars["lower"] + 1
        elif char in CHARACTERS["upper"]:
            included_chars["upper"] = included_chars["upper"] + 1
        elif char in CHARACTERS["digit"]:
            included_chars["digit"] = included_chars["digit"] + 1
        elif char in CHARACTERS["symbol"]:
            included_chars["symbol"] = included_chars["symbol"] + 1
        elif char in CHARACTERS["extended"]:
            included_chars["extended"] = included_chars["extended"] + 1

    if included_chars["lower"] < atleast:
        return False
    if included_chars["upper"] < atleast:
        return False
    if included_chars["digit"] < atleast:
        return False

    if not nosymbols:
        if included_chars["symbol"] < atleast:
            return False

    if extended:
        if included_chars["extended"] < atleast:
            return False

    return True


def genpwd(length: int = 32, nosymbols: bool = False, extended: bool = False, nocolor: bool = False) -> str:
    chars = CHARACTERS["lower"] + CHARACTERS["upper"] + CHARACTERS["digit"]

    if not nosymbols:
        chars = chars + CHARACTERS["symbol"]

    if extended:
        chars = chars + CHARACTERS["extended"]

    length = min(max(16, length), 128)

    while True:
        result = "".join([secrets.choice(chars) for _ in range(length)])

        if is_strong(result, nosymbols, extended, length, 1):
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
        "-e",
        "--extended",
        action="store_true",
        help="include special latin-1 supplement characters",
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

    for _ in range(min(max(1, args.count), 20)):
        print(genpwd(args.length, args.nosymbols, args.extended, args.nocolor))


if __name__ == "__main__":
    main()
