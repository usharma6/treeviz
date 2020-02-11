import igraph
import sys
from igraph import *
sys.path.insert(1, 'io')
from parser import parse_file
from options import get_args

def make_graph(args):
    filename = args.input
    vertex_dict, edges = parse_file(filename)
    graph = Graph()
    graph.add_vertices(len(vertex_dict.keys()))
    graph.vs["name"] = list(vertex_dict.values())
    #for key in vertex_dict.keys():
       # graph.vs["name"].append(vertex_dict[key])
    graph.add_edges(edges)
    return graph

if __name__ == "__main__":
    args = get_args()
    graph = make_graph(args)
    layout = graph.layout("rt", root = [0])
    visual_style = {}
    visual_style["layout"] = layout
    visual_style["vertex_label"] = graph.vs["name"] 
    visual_style["margin"] = 50
    visual_style["vertex_size"] = 50
    visual_style["vertex_label_dist"] = 1
    visual_style["bbox"] = (2000,2000)
    visual_style["vertex_color"] = "green"
    plot(graph, **visual_style) 

