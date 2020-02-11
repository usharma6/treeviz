import sys
from options import get_args
import re

def parse_file(filename):
    path_splitter = re.compile(':\\s+')
    line_splitter = re.compile(',\\s+')
    vertex_dict = {}
    edges = []
    previous_level = []
    cur_level = []
    vertex_number = 0
    count = 0
    with open(filename, 'rt') as fp: 
        line = fp.readline()
        while line:
            if vertex_number == 0:
                vertex_dict[vertex_number] = line
                cur_level.append(vertex_number)
                vertex_number += 1
            elif len(line) > 1:
                paths = path_splitter.split(line)
                print(len(paths))
                print(paths)
                for i in range(len(paths)):
                    vertices = line_splitter.split(paths[i])
                    for vertex in vertices:
                        vertex_dict[vertex_number] = vertex
                        edges.append((previous_level[i], vertex_number))
                        cur_level.append(vertex_number)
                        vertex_number += 1
            previous_level = [i for i in cur_level]
            cur_level = []
            line = fp.readline()
    return vertex_dict, edges

if __name__ == "__main__":
    ARGS = get_args()
    dict_output, edges = parse_file(ARGS.input)
    print(dict_output)
    print(edges)
