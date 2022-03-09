import argparse
import logging

import sys

parser = argparse.ArgumentParser()

parser.add_argument("-v",
                    "--verbose",
                    help="increase output verbosity",
                    action="store_true")

parser.add_argument("-d",
                    "--debug",
                    help="increase output verbosity to debug mode",
                    action="store_true")

parser.add_argument("-k",
                    "--keep",
                    help="increase output verbosity to debug mode",
                    action="store_true")

args = parser.parse_args()

if len(sys.argv) > 0 and (sys.argv[0] == "-h" or sys.argv[0] == "--help"):
    parser.print_help()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

if args.verbose:
    logging.basicConfig(level=logging.INFO)
