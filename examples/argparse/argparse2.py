#!/usr/bin/env python

import argparse

# prog = sys.argv[0], you could change if you want, prog="myprogram"
parser = argparse.ArgumentParser(description='Description',
                                 version="%(prog)s 0.1",
                                 epilog="Epilogue")
parser.parse_args()