import secrets
from .constants import (
    CHARACTERS,
    COLORS_MAP,
    DEFAULT_LENGTH,
    DEFAULT_WORDS,
    IS_ATTY,
    MAX_LENGTH,
    MAX_WORDS,
    MIN_LENGTH,
    MIN_WORDS,
)
from .words import EFF_LONG_WORDS


def apply_color(chars: str) -> str:
    return "".join(f"\033[{COLORS_MAP.get(char, '00')}m{char}\033[00m" for char in chars)


def genpwd_password(
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


def genpwd_passphrase(
    length: int = DEFAULT_WORDS, capitalize: bool = False, nocolor: bool = False
) -> str:
    words: list[str] = EFF_LONG_WORDS

    length = min(max(MIN_WORDS, length), MAX_WORDS)

    if capitalize:
        result = [secrets.choice(words).capitalize() for _ in range(length)]
    else:
        result = [secrets.choice(words) for _ in range(length)]

    if not nocolor and IS_ATTY:
        return "\033[02m-\033[00m".join(result)
    else:
        return "-".join(result)


def genpwd_username(capitalize: bool = False, nocolor: bool = False) -> str:
    words: list[str] = EFF_LONG_WORDS

    result = secrets.choice(words)
    digit = "".join(secrets.choice(CHARACTERS["digit"]) for _ in range(4))

    if capitalize:
        result = result.capitalize()

    if not nocolor and IS_ATTY:
        return result + apply_color(digit)
    else:
        return result + digit
