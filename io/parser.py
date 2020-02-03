import sys
from options import get_args

def parse_file(filename):
    print(filename)

if __name__ == "__main__":
    ARGS = get_args()
    parse_file(ARGS.input)
