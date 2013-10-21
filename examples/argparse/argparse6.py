
#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group(required=True)
group1.add_argument("-a", "--argument-A", action="store_true")
group1.add_argument("-b", "--argument-B", action="store_false")

group2 = parser.add_mutually_exclusive_group(required=True)
group2.add_argument("-c", "--argument-C", help="c help")
group2.add_argument("-d", "--argument-D", help="d help")

parser.parse_args()