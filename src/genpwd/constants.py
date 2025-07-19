VERSION = "1.8.0"

DEFAULT_LENGTH = 32
MIN_LENGTH = 16
MAX_LENGTH = 128

CHARACTERS = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digit": "0123456789",
    "symbol": "!#$%&()*+,-.:;<=>?@^_/|[]{}~",  # Excluded "'`\
    "extended": "".join(
        [chr(cp) for cp in range(0xC0, 0xFF + 1)]
    ),  # Latin-1 Supplement
}