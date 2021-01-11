from src.DiGraph import DiGraph
import random


def graph_creator(v_size: int, e_size: int = 0) -> DiGraph:
    e_size = int(e_size)
    graph = DiGraph()
    for i in range(v_size):
        graph.add_node(i)

    for i in range(e_size):
        a = random.randint(0, v_size)
        b = random.randint(0, v_size)
        w = random.uniform(0.1, 10)
        graph.add_edge(a, b, w)
    return graph
