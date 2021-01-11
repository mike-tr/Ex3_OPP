from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.utilities.Jsonconverter import load_networkx_graph
import networkx as nx
import time

graph: DiGraph = None
algo: GraphAlgo = None
v = 100000
e = v * 10

# path = "../../data/G_20000_160000_0.json"
# path = "../../data/G_20000_160000_0.json"
path = "../../data/G_30000_240000_0.json"
save = e < 5000001


def test_load():
    global algo
    algo = GraphAlgo()
    algo.load_from_json(path)


if __name__ == '__main__':
    t = time.time()
    test_load()
    print(algo.get_graph())
    print(time.time() - t)

    t = time.time()
    algo.connected_components()
    # print(algo.connected_components())
    print(time.time() - t)

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
    print(time.time() - t)

    # print(nx.shortest_path_length(nx_graph, 0, 100, 'weight'))

    t = time.time()
    # components = nx.connected_components(nx_graph)
    # nx.connected_components(nx_graph)
    list(nx.strongly_connected_components(nx_graph))
    # c = sorted(nx.strongly_connected_components(nx_graph), key=len, reverse=True)
    print(time.time() - t)
    # print(c)
