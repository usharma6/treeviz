import igraph
from igraph import *

def main():
    testgraph = Graph()
    testgraph.add_vertices(3)
    testgraph.vs["names"] = ["canny fanny", "kitty kitty lick lick", "shwoopers"]
    layout = testgraph.layout("rt", 2)
    plot(testgraph, layout = layout)
    

if __name__ == "__main__":
    main()
