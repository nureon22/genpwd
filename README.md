# Generate secure password from terminal

This is a very simple python project that generate a strong and secure password from terminal.

## Installation

### Using pip

```sh
pip install "git+https://github.com/nureon22/genpwd.git"
```

### Using pipx

```sh
pipx install "git+https://github.com/nureon22/genpwd.git"
```

## Usages

```sh
usage: genpwd [-h] [--passphrase] [-C] [-D] [-S] [-e] [-l LENGTH] [-w WORDS]
              [-n COUNT] [-v]

Generate very strong passwords

options:
  -h, --help            show this help message and exit
  --passphrase          Generate passphrase instead of password
  -C, --nocolor         print passwords in no color
  -D, --nodigits        exclude digits
  -S, --nosymbols       exclude special symbol characters
  -e, --extended        include special latin-1 supplement characters
  -l LENGTH, --length LENGTH
                        password length (from 8 to 128)
  -w WORDS, --words WORDS
                        Number of words for passphrase (from 4 to 128)
  -n COUNT, --count COUNT
                        numbers of passwords to generate (from 1 to 20)
  -v, --version         print version number and exit
```
