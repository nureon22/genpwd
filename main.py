#!/bin/env python3

import sys, argparse
from math import floor
from random import random


VERSION="1.2.0"


def random_int(length: int):
    return floor(random() * length)


def genpwd(length: int, nosymbols: bool, colored: bool):
    all_chars = {
        "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lower": "abcdefghijklmnopqrstuvwxyz",
        "number": "0123456789",
        "symbol": "~`!@#$%^&*_-+=:;<>,.?/(){}[]"
    }
    colors = [["upper", 93], ["lower", 92], ["number", 94], ["symbol", 95]]

    if nosymbols:
        del all_chars["symbol"]
        colors.pop()

    chars_list = "".join(all_chars.values())

    length = min(max(8, length), 60)
    result = []

    lastchar_category = None

    while length:
        char = chars_list[random_int(len(chars_list))]

        for [category, color] in colors:

            # Find out the category of randomly picked character
            if char in all_chars[category]:

                # If the last character's category is same as current, regenerate
                if lastchar_category == category:
                    length = length + 1
                    break
                else:
                    lastchar_category = category

                    if colored:
                        result.append("\033[{}m{}\033[00m".format(color, char))
                    else:
                        result.append(char)

                    # Remove randomly picked character from chars_list
                    # to prevent duplicate characters in final result
                    chars_list = chars_list.replace(char, "")

        length = length - 1

    print("".join(result))


def main():
    arg_parser = argparse.ArgumentParser(
            prog="genpwd",
            description="Generate very strong passwords"
    )
    arg_parser.add_argument("-C", "--nocolor", action="store_true", help="print passwords in no color")
    arg_parser.add_argument("-S", "--nosymbols", action="store_true", help="exclude special symbol characters")
    arg_parser.add_argument("-l", "--length", action="store", type=int, default=32, help="password length (from 8 to 60)")
    arg_parser.add_argument("-n", "--count", action="store", type=int, default=1, help="numbers of passwords to generate (from 1 to 20)")
    arg_parser.add_argument("-v", "--version", action="store_true", help="print version number and exit")
    args = arg_parser.parse_args()

    if args.version:
        return print(VERSION)

    if args.count:
        for index in range(min(max(1, args.count), 20)):
            genpwd(length=args.length, colored=not args.nocolor, nosymbols=args.nosymbols)
    else:
        genpwd(length=args.length, colored=not args.nocolor, nosymbols=args.nosymbols)


if __name__ == "__main__":
    main()
