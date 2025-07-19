import sys

VERSION = "1.9.1"

DEFAULT_LENGTH = 32
MIN_LENGTH = 16
MAX_LENGTH = 128

DEFAULT_WORDS = 8
MIN_WORDS = 4
MAX_WORDS = 128

CHARACTERS = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digit": "0123456789",
    "symbol": "!#$%&()*+,-.:;<=>?@^_/|[]{}~",  # Excluded "'`\
    "extended": "".join(
        [chr(cp) for cp in range(0xC0, 0xFF + 1)]
    ),  # Latin-1 Supplement
}

COLORS_MAP = {}

for char in CHARACTERS["lower"]: COLORS_MAP[char] = "92"
for char in CHARACTERS["upper"]: COLORS_MAP[char] = "93"
for char in CHARACTERS["digit"]: COLORS_MAP[char] = "94"
for char in CHARACTERS["symbol"]: COLORS_MAP[char] = "95"
for char in CHARACTERS["extended"]: COLORS_MAP[char] = "91"

IS_ATTY = sys.stdout.isatty()
