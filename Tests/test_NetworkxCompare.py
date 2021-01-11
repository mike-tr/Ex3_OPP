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
        file = "../data/G_100_800_0.json"
        s = 0
        f = 9
        print(file)
        nx_graph = load_networkx_graph(file)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(file)
        # t = time.time()
        # print((nx.shortest_path_length(nx_graph, s, f, 'weight'), nx.dijkstra_path(nx_graph, s, f, 'weight')))
        # print("NetworkX time: ", time.time() - t)
        # t = time.time()
        # print(graph_algo.shortest_path(s, f))
        # print("DiGraph time: ", time.time() - t)
        t = time.time()
        list(nx.strongly_connected_components(nx_graph))
        print("Networkx scc time (list): ", time.time() - t)
        t = time.time()
        sorted(nx.strongly_connected_components(nx_graph), key=len, reverse=True)
        # print("Networkx scc time: ", time.time() - t)
        print(nx.node_connected_component(nx_graph, 0))
        t = time.time()
        print(graph_algo.connected_component(0))
        # graph_algo.connected_components()
        print("DiGraph scc time: ", time.time() - t)

    def test_create_graph(self):
        v = 1000000
        e = v * 10
        graph = graph_creator(v, e)
        graph_algo = GraphAlgo(graph)
        graph_algo.save_to_json("../data/Huge_graph.json")

    def test_load_from_json(self):
        file = "../Data/Huge_graph.json"
        graph_algo = GraphAlgo()
        t = time.time()
        graph_algo.load_from_json(file)
        print("Digraph loading time: ", time.time() - t)
        t = time.time()
        load_networkx_graph(file)
        print("Networkx loading time: ", time.time() - t)
        print(graph_algo.get_graph())
