import argparse as ap

def get_args():
    args = ap.ArgumentParser()
    args.add_argument('--input', type = str, default = 'examples/input/climb_tree.txt')
    return args.parse_args()
