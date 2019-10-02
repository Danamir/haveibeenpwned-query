#!/usr/bin/env python3
"""!!DEPRECATED!! The Have I been pwned account API is now covered by a $3.5/month fee
and is no longer supported by this script.

Have I been Pwned account database check.

Usage: pwned-account [--help] [options] [ACCOUNT]

Arguments:
  ACCOUNT               The account to check, if empty prompt for account.

Options:
  -d --debug            Debug only (displays informations and quits).
  -h --help             Displays the help.
  -v --verbose          Displays more informations.
"""

import sys
import hashlib
import json
import re

import requests
import docopt as docpt

from docopt import docopt

# options
options = None  # type: dict
debug = False  # type: bool
verbose = False  # type: bool

# arguments
account = ""  # type: str


def main():
    """Main method."""

    # options
    global debug, verbose
    debug, verbose = options['--debug'], options['--verbose']  # type: bool, bool

    if debug:
        verbose = True

    # arguments
    global account
    account = options['ACCOUNT']  # type: str

    if not account:
        account = input('Account: ')
        print()

    if not account:
        raise RuntimeWarning('Empty account.')

    # API URL
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/%s' % account

    # verbose
    if verbose:
        print('API URL %s' % url)
        print()

    # fetch matching hashes
    r = requests.get(url)

    #  handle HTTP errors
    if not r.ok:
        print('Wrong API response, HTTP status code: %s' % r.status_code)
        print(r.content)
        exit(1)

    pwns = json.loads(r.content or '{}')

    if debug:
        print(json.dumps(pwns, indent=4))

    # output
    if not pwns:
        print('Account not pwned.')
    else:
        print('Pwned in %d breach%s:' % (len(pwns), 'es' if len(pwns) > 1 else ''))
        idx = 0
        for pwned in pwns:  # type: dict
            idx = idx + 1
            label = pwned.get('Title', None)

            if verbose:
                desc = pwned.get('Description', '')
                desc = re.sub(r'<a.*>(.*)</a>', r'\g<1>', desc)
                
                label = '%s: %s' % (label, desc)
                label = '%s\n       [%s]' % (label, ', '.join(pwned.get('DataClasses', [])))

            print('%5d. %s' % (idx, label))

            if verbose:
                print()
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
