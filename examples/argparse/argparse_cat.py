#!/usr/bin/env python

import argparse

# prog = sys.argv[0], you could change if you want, prog="myprogram"
parser = argparse.ArgumentParser(description='Concatenate FILE(s), or standard input, to standard output.',
                                 version="%(prog)s 8.20",
                                 usage="cat [OPTION]... [FILE]...",
                                 epilog="""With no FILE, or when FILE is -, read standard input.\n
Examples:
  cat f - g  Output f's contents, then standard input, then g's contents.
  cat        Copy standard input to standard output.

Report cat bugs to bug-coreutils@gnu.org
GNU coreutils home page: <http://www.gnu.org/software/coreutils/>
General help using GNU software: <http://www.gnu.org/gethelp/>
For complete documentation, run: info coreutils 'cat invocation'""")

parser.add_argument("-A", "--show-all", 
                    help="equivalent to -vET",
                    action="store_true")
parser.add_argument("-b", "--number-nonblank", 
                    help="number nonempty output lines, overrides -n",
                    action="store_true")
parser.add_argument("-e",  
                    help="equivalent to -vE",
                    action="store_true")

parser.parse_args()