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
Usage: genpwd [-h] [-C] [-S] [-l LENGTH] [-n COUNT] [-v]

Generate very strong passwords

Options:
  -h, --help            show this help message and exit
  -C, --nocolor         print passwords in no color
  -S, --nosymbols       exclude special symbol characters
  -l LENGTH, --length LENGTH
                        password length (from 16 to 128)
  -n COUNT, --count COUNT
                        numbers of passwords to generate (from 1 to 20)
  -v, --version         print version number and exit
```
