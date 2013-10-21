#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')

parser.parse_args()