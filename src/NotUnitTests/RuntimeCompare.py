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

tries = 25


def test_load(file):
    global algo
    algo = GraphAlgo()
    algo.load_from_json(file)


def do_test(file):
    t = time.time()
    print("\n-----------", file, "--------------")
    print("- python -")
    test_load(file)
    print(algo.get_graph())

    print("python load time:", time.time() - t)

    print("\n- nx -")
    t = time.time()
    nx_graph = load_networkx_graph(file)
    print("NetworkX load:", time.time() - t)

    print("- - - - - - - - - - -")
    print("compute avg path time:")
    print("- python -")
    t = time.time()

    # print(algo.shortest_path(0, 1000))

    fail = 0
    avg_dist = 0
    for i in range(tries):
        dist = algo.shortest_path(0, i + 1)
        if dist[0] == float("inf"):
            fail += 1
        else:
            avg_dist += dist[0]

    end_time = time.time() - t
    print("python avg dist:", avg_dist / tries)
    print("python run:", tries, ",number of times path not found:", fail)
    print("python avg path compute time:", end_time / tries)

    print("\n- nx -")

    t = time.time()
    # components = nx.connected_components(nx_graph)
    # nx.connected_components(nx_graph)

    fail = 0
    avg_dist = 0
    for i in range(tries):
        old = time.time()
        try:
            avg_dist += nx.shortest_path_length(nx_graph, 0, i + 1, 'weight')

            # print("netx path dist : ", nx.shortest_path_length(nx_graph, 0, i, 'weight'))
        except:
            fail += 1
            # print("no path")
            pass
        # print(time.time() - old)
    end_time = time.time() - t
    print("NetworkX avg dist:", avg_dist / tries)
    print("NetworkX run:", tries, ",number of times path not found:", fail)
    print("NetworkX avg path compute time:", end_time / tries)

    print("- - - - - - - - - - -")
    print("compute single component time:")
    print("- python -")
    g = GraphAlgo(algo.get_graph())
    t = time.time()

    avg_len = 0
    for i in range(tries):
        avg_len += len(g.connected_component(i))
    end_time = time.time() - t
    print("python avg single component length:", avg_len / tries)
    # print(g.connected_component(0))
    print("python avg single component compute time:", end_time / tries)

    print("- - - - - - - - - - -")
    print("compute components time:")
    print("- python -")

    t = time.time()
    for i in range(tries):
        c = g.connected_components()
    end_time = time.time() - t
    print("python number of components:", len(c))
    print("python components avg compute time:", end_time / tries)

    print("\n- nx -")

    t = time.time()
    # components = nx.connected_components(nx_graph)
    # nx.connected_components(nx_graph)
    for i in range(tries):
        c = sorted(nx.strongly_connected_components(nx_graph), key=len, reverse=True)
    end_time = time.time() - t
    print("NetworkX number of components:", len(c))
    print("NetworkX components avg compute time:", end_time / tries)


if __name__ == '__main__':
    directory = "../../data_local/"
    # do_test(directory + "g_100k_5m")
    # arr = ["g_100k_100k", "g_100k_1m", "g_100k_5m", "g_1m_0", "g_1m_1m", "g_1m_10m"]
    directory = "../../data/"
    arr = ["G_10_80_0.json", "G_100_800_0.json", "G_1000_8000_0.json", "G_10000_80000_0.json",
           "G_20000_160000_0.json", "G_30000_240000_0.json"]
    for name in arr:
        do_test(directory + name)
