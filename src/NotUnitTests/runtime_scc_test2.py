from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.utilities.Jsonconverter import load_networkx_graph
import networkx as nx
import time
from Tests.dummyGraph import graph_creator

graph: DiGraph = None
algo: GraphAlgo = None
v = 1000000
e = v * 1

path = "../../data/my_graph"


# path = "../../data/G_20000_160000_0.json"
# path = "../../data/G_30000_240000_0.json"

def test_create():
    global algo
    dummy = graph_creator(v, e)
    dummy.add_edge(0, 1, 1)
    dummy.add_edge(1, 0, 1)

    dummy.add_edge(2, 3, 1)
    dummy.add_edge(3, 2, 1)
    algo = GraphAlgo(dummy)
    algo.save_to_json(path)
    algo.load_from_json(path)


if __name__ == '__main__':
    t = time.time()
    test_create()
    print(algo.get_graph())
    print("DiGraph load:", time.time() - t)

    t = time.time()
    algo.connected_components()
    # print(algo.connected_components())
    print("DiGraph components:", time.time() - t)

    scc_components = []
    scc: list
    for scc in algo.connected_components():
        scc_components.append(sorted(scc))
    c = sorted(scc_components, key=len, reverse=True)
    # print(c)

    print("------------- nx -----------")
    t = time.time()
    nx_graph = load_networkx_graph(path)
    print(len(nx_graph.edges))
    print("NetworkX load:", time.time() - t)

    # print(nx.shortest_path_length(nx_graph, 0, 100, 'weight'))

    t = time.time()
    # components = nx.connected_components(nx_graph)
    # nx.connected_components(nx_graph)
    c = sorted(nx.strongly_connected_components(nx_graph), key=len, reverse=True)
    print("NetworkX components:", time.time() - t)
    # print(c)
