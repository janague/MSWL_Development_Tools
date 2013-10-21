#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
# A optional argument A with necessary value
parser.add_argument("-a", "--argument-A", 
                    help="Information about argument with pattern [-a ARGUMENT]")
# A optional argument B without necessary value
parser.add_argument("-b", "--argument-B", 
                    help="Information about b argument with pattern [-b] ",
                    action="store_true")
parser.parse_args()