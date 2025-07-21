#!/bin/env python3

import argparse, secrets
from .constants import (
    CHARACTERS,
    COLORS_MAP,
    IS_ATTY,
    VERSION,
    DEFAULT_LENGTH,
    MIN_LENGTH,
    MAX_LENGTH,
    DEFAULT_WORDS,
    MIN_WORDS,
    MAX_WORDS,
)
from .words import EFF_LONG_WORDS


def apply_color(chars: str) -> str:
    return "".join(
        "\033[{}m{}\033[00m".format(COLORS_MAP.get(char, "00"), char) for char in chars
    )


def genpwd(
    length: int = DEFAULT_LENGTH,
    digits: bool = False,
    symbols: bool = False,
    extended: bool = False,
    nocolor: bool = False,
) -> str:
    groups = ["lower", "upper"]

    if digits:
        groups.append("digit")
    if symbols:
        groups.append("symbol")
    if extended:
        groups.append("extended")

    chars = "".join(CHARACTERS[group] for group in groups)

    length = min(max(MIN_LENGTH, length), MAX_LENGTH)

    while True:
        result = "".join(secrets.choice(chars) for _ in range(length))

        # Check generated password contains atleast one character from every group
        if all(any(char in CHARACTERS[group] for char in result) for group in groups):
            break

    if not nocolor and IS_ATTY:
        return apply_color(result)
    else:
        return result


def genpwd_passphrase(length: int = DEFAULT_WORDS, nocolor: bool = False) -> str:
    words: list[str] = EFF_LONG_WORDS

    length = min(max(MIN_WORDS, length), MAX_WORDS)
    result = [secrets.choice(words) for _ in range(length)]

    if not nocolor and IS_ATTY:
        return "\033[02m-\033[00m".join(result)
    else:
        return "-".join(result)


def genpwd_username(nocolor: bool = False) -> str:
    words: list[str] = EFF_LONG_WORDS

    result = secrets.choice(words) + "".join(secrets.choice(CHARACTERS["digit"]) for i in range(4))

    if not nocolor and IS_ATTY:
        return apply_color(result)
    else:
        return result


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        prog="genpwd", description="Generate very strong passwords"
    )
    arg_parser.add_argument(
        "--passphrase",
        action="store_true",
        help="Generate passphrase instead of password",
    )
    arg_parser.add_argument(
        "--username",
        action="store_true",
        help="Generate username instead of password",
    )
    arg_parser.add_argument(
        "-C", "--nocolor", action="store_true", help="print passwords in no color"
    )
    arg_parser.add_argument(
        "-D",
        "--nodigits",
        action="store_true",
        help="exclude digits",
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
        default=DEFAULT_LENGTH,
        help="password length (from {} to {})".format(MIN_LENGTH, MAX_LENGTH),
    )
    arg_parser.add_argument(
        "-w",
        "--words",
        action="store",
        type=int,
        default=DEFAULT_WORDS,
        help="Number of words for passphrase (from {} to {})".format(
            MIN_WORDS, MAX_WORDS
        ),
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

    if args.passphrase:
        for _ in range(count):
            print(
                genpwd_passphrase(args.words, args.nocolor),
                end=("\n" if IS_ATTY else ""),
            )
    elif args.username:
        for _ in range(count):
            print(
                genpwd_username(args.nocolor),
                end=("\n" if IS_ATTY else ""),
            )
    else:
        for _ in range(count):
            print(
                genpwd(args.length, not args.nodigits, not args.nosymbols, args.extended, args.nocolor),
                end=("\n" if IS_ATTY else ""),
            )


if __name__ == "__main__":
    main()
