from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time

graph: DiGraph = None
algo: GraphAlgo = None
v = 100000
e = v * 10

path = "../../data/G_10000_80000_0.json"
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
    print(algo.connected_components())
    print(time.time() - t)
