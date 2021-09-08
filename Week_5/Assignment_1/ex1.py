import argparse

import argparse
parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument("num", type=int, help="input the number")
parser.add_argument("--verbosity", action="store_true",
help="readable")
args = parser.parse_args()
if args.verbosity:
    print("The square is: ", args.num**2)
else:
    print(args.num**2)
