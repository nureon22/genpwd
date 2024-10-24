#!/bin/env python3

import sys
from math import floor
from random import random


def random_int(length: int):
    return floor(random() * length)


def main():
    all_chars = {
        "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lower": "abcdefghijklmnopqrstuvwxyz",
        "number": "0123456789",
        "symbol": "~`!@#$%^&*_-+=:;<>,.?/(){}[]"
    }
    chars_list = "".join(all_chars.values())

    length = 32
    result = []

    lastchar_category = None

    while length:
        char = chars_list[random_int(len(chars_list))]

        for [category, color] in [["upper", 93], ["lower", 92], ["number", 94], ["symbol", 95]]:

            # Find out the category of randomly picked character
            if char in all_chars[category]:

                # If the last character's category is same as current, regenerate
                if lastchar_category == category:
                    length = length + 1
                    break
                else:
                    lastchar_category = category
                    result.append("\033[{}m{}\033[00m".format(color, char))

                    # Remove randomly picked character from chars_list
                    # to prevent duplicate characters in final result
                    chars_list = chars_list.replace(char, "")

        length = length - 1

    print("".join(result))


if __name__ == "__main__":
    main()
