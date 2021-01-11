from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time
import networkx as nx
from src.utilities.Jsonconverter import load_networkx_graph

graph: DiGraph = None
algo: GraphAlgo = None
v = 100000
e = v * 10

path = "../../MyGraph"
save = e < 5000001


def test_load(file):
    global algo
    algo = GraphAlgo()
    algo.load_from_json(file)


def do_test(file):
    t = time.time()
    print("-----------", file, "--------------")
    test_load(file)
    print(algo.get_graph())
    print("python load time:", time.time() - t)

    t = time.time()
    print(algo.shortest_path(0, 1000))
    print("python path time:", time.time() - t)

    g = GraphAlgo(algo.get_graph())
    t = time.time()
    g.connected_component(0)
    # print(g.connected_component(0))
    print("python single_scc time:", time.time() - t)
    print("------------- nx -----------")
    t = time.time()
    nx_graph = load_networkx_graph(file)
    print(len(nx_graph.edges))
    print("NetworkX load:", time.time() - t)

    t = time.time()
    # components = nx.connected_components(nx_graph)
    # nx.connected_components(nx_graph)
    try:
        print(nx.shortest_path_length(nx_graph, 0, 1000, 'weight'))
    except:
        print("no path")
        pass
    print("NetworkX components:", time.time() - t)


if __name__ == '__main__':
    directory = "../../data_local/"
    do_test(directory + "g_100k_5m")
    # arr = ["g_100k_100k", "g_100k_1m", "g_100k_5m", "g_1m_0", "g_1m_1m", "g_1m_10m"]
    # for name in arr:
    #     do_test(directory + name)
