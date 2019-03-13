#!python
"""Have I been Pwned password database check.

Usage: pwned-password [--help] [options] [PASSWORD]

Arguments:
  PASSWORD              The password to check, if empty prompt for password.

Options:
  -d --debug            Debug only (displays informations and quits).
  -h --help             Displays the help.
  -v --verbose          Displays more informations.
"""

import sys
import hashlib
from getpass import getpass

import requests
import docopt as docpt

from docopt import docopt

# options
options = None  # type: dict
debug = False  # type: bool
verbose = False  # type: bool

# arguments
password = ""  # type: str


def main():
    """Main method."""

    # options
    global debug, verbose
    debug, verbose = options['--debug'], options['--verbose']  # type: bool, bool

    if debug:
        verbose = True

    # arguments
    global password
    password = options['PASSWORD']  # type: str

    if not password:
        password = getpass('Password: ')
        print()

    if not password:
        raise RuntimeWarning('Empty password.')

    # SHA-1 hash password
    password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    password = ''

    password_hash_prefix = password_hash[:5]
    password_hash_suffix = password_hash[5:]

    # API URL
    url = 'https://api.pwnedpasswords.com/range/%s' % password_hash_prefix

    # verbose
    if verbose:
        print('Password hash split: %s %s' % (password_hash_prefix, password_hash_suffix))
        print('API URL %s' % url)
        print()

    # fetch matching hashes
    r = requests.get(url)

    pwned_hashes = {}
    for pwned_hash in r.content.decode().split('\r\n'):
        if debug:
            print(pwned_hash)

        h, n = pwned_hash.split(':')
        pwned_hashes[h] = n

    # look for hash suffix
    pwned = pwned_hashes.get(password_hash_suffix, None)

    # output
    if pwned is None:
        print('Password not pwned.')
    else:
        print('Password pwned, %s occurences.' % pwned)
    print()


def cli():
    """Command-line interface"""
    global options
    options = docopt(__doc__)
    try:
        main()
    except RuntimeWarning as w:
        print("  Warning: %s" % w, file=sys.stderr)
        sys.exit(1)
    except RuntimeError as w:
        print("%s" % w, file=sys.stderr)
        print(docpt.printable_usage(__doc__))
        sys.exit(1)


# main entry point
if __name__ == '__main__':
    cli()
