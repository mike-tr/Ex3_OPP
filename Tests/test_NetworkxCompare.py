from unittest import TestCase
from src.DiGraph import DiGraph
import networkx as nx
import random
from Tests.dummyGraph import graph_creator
from src.utilities.Jsonconverter import load_networkx_graph
import matplotlib.pyplot as plt


class TestGraphAlgo(TestCase):
    def test_graph_nx(self):
        random.seed(42)
        nx_graph = load_networkx_graph("../data/A0")
        nx.draw(nx_graph)
        plt.show()


    def test_create_graph(self):
        random.seed(42)
        graph = DiGraph()
        v = 100000
        e = v * 10
        for i in range(v):
            graph.add_node(i)
        while graph.e_size() < e:
            a = random.randint(0, v)
            b = random.randint(0, v)
            w = random.uniform(0.1, 10)
            graph.add_edge(a, b, w)
