#!/bin/env python3

import argparse
from .constants import (
    DEFAULT_LENGTH,
    DEFAULT_WORDS,
    IS_ATTY,
    MAX_GENERATION,
    MAX_LENGTH,
    MAX_WORDS,
    MIN_LENGTH,
    MIN_WORDS,
    VERSION,
)
from .genpwd import genpwd_username, genpwd_passphrase, genpwd_password


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
        "-c", "--capitalize", action="store_true", help="Capitalize passphrase and username"
    )
    arg_parser.add_argument(
        "-U",
        "--noupper",
        action="store_true",
        help="exclude uppercase characters",
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
        help=f"password length (from {MIN_LENGTH} to {MAX_LENGTH})",
    )
    arg_parser.add_argument(
        "-w",
        "--words",
        action="store",
        type=int,
        default=DEFAULT_WORDS,
        help=f"Number of words for passphrase (from {MIN_WORDS} to {MAX_WORDS})",
    )
    arg_parser.add_argument(
        "-n",
        "--count",
        action="store",
        type=int,
        default=1,
        help=f"numbers of passwords to generate (from 1 to {MAX_GENERATION})",
    )
    arg_parser.add_argument(
        "-v", "--version", action="store_true", help="print version number and exit"
    )
    args = arg_parser.parse_args()

    if args.version:
        return print(VERSION)

    count = min(max(1, args.count), MAX_GENERATION)
    results: list[str] = []

    if args.passphrase:
        for _ in range(count):
            results.append(
                genpwd_passphrase(args.words, args.capitalize, args.nocolor),
            )
    elif args.username:
        for _ in range(count):
            results.append(
                genpwd_username(args.capitalize, args.nocolor),
            )
    else:
        for _ in range(count):
            results.append(
                genpwd_password(
                    args.length, not args.noupper, not args.nodigits, not args.nosymbols, args.extended, args.nocolor
                ),
            )

    print("\n".join(results), end=("\n" if IS_ATTY else ""))


if __name__ == "__main__":
    main()
