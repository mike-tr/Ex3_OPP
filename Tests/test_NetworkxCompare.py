from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx
import random
from Tests.dummyGraph import graph_creator
from src.utilities.Jsonconverter import load_networkx_graph
import matplotlib.pyplot as plt
import time


class TestGraphAlgo(TestCase):
    def test_graph_nx(self):
        file = "../data/G_30000_240000_0.json"
        s = 0
        f = 29999
        print(file)
        nx_graph = load_networkx_graph(file)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(file)
        t = time.time()
        print((nx.shortest_path_length(nx_graph, s, f, 'weight'), nx.dijkstra_path(nx_graph, s, f, 'weight')))
        print("NetworkX time: ", time.time() - t)
        t = time.time()
        print(graph_algo.shortest_path(s, f))
        print("DiGraph time: ", time.time() - t)

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
