#!/bin/python3

from math import floor
from random import random
from sys import argv
import re


def clamp(minimum: int, prefered: int, maximum: int):
    return min(max(minimum, prefered), maximum)


def genpwd(length: int):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*<>,.:;?_-+=([{}])"
    chars_length = len(chars)
    result = []

    for index in range(length):
        result.append(chars[floor(random() * chars_length)])

    return "".join(result)


def main():
    length = 16

    if len(argv) > 1 and re.search(r"^[0-9]+$", argv[1]):
        length = clamp(8, int(argv[1]), 512)

    print(genpwd(length))


if __name__ == "__main__":
    main()
