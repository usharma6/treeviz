import argparse as ap

def get_args():
    args = ap.ArgumentParser()
    args.add_argument('--input', type = str, default = 'MyTrees/Climbing/outside_2.txt')
    return args.parse_args()
