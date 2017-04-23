#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyEmT is a python/emacs tiny syntax checker.

It is a wrapper script which makes it easy to use flymake to run various
syntax checking tools on your code. Since flymake expects to just run
the script with the filename and no other arguments, this file is mainly
expected to be run with only one argument: the target file to check.

It runs the various checkers (currently pylint and pep8) and writes the
results to standard output in a format that the emacs flymake package
can read.

See the
[https://github.com/emin63/pyempt/blob/master/README.md](README.md)
file on github or accompanying this distribution for more details and
how to setup flymake in emacs to use this.

See the [https://github.com/emin63/pyempt/blob/master/LICENSE](LICENSE)
file for the BSD 2-clause simplified license. Basically this is open
source and you can modify freely provided credit is given to the author(s).
"""


import subprocess
import argparse

def make_parser():
    """Make the parser to process the command line.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='Target file to check.')
    return parser

def run_checkers(args):
    """Do the work of running the various checkers.
    """
    result = []
    pep8_cmd = ['pep8', args.target]
    pylint_cmd = ['pylint', args.target, '-f', 'parseable', '-r', 'n',
                  '--include_ids=y']
    cmd_list = [pep8_cmd, pylint_cmd]
    for my_cmd in cmd_list:
        my_process = subprocess.Popen(my_cmd, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        output = my_process.stdout.read()
        result.append(output.decode('utf8'))
    return result


def main():
    """Run the main program.

    This is the main entry point executed when the script is run.
    """
    parser = make_parser()
    args = parser.parse_args()
    result = run_checkers(args)
    print('\n'.join(result))

if __name__ == '__main__':
    main()
