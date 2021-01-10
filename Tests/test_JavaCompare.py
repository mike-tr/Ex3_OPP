from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from Tests.dummyGraph import graph_creator


class TestGraphAlgo(TestCase):

    def test_create_graph(self):
        graph_algo = GraphAlgo(graph_creator(100000, 300000))
        graph_algo.save_to_json("../data/huge_random_graph.json")

    def test_a0(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A0")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(1, 5))
        # print(graph_algo.shortest_path(0, 6))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(1))

    def test_a1(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A1")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(2, 12))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(7))

    def test_a2(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A2")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(12, 3))
        # print(graph_algo.shortest_path(29, 11))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(2))

    def test_a3(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A3")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(40, 31))
        # print(graph_algo.shortest_path(8, 17))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(30))

    def test_a4(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A4")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(30, 17))
        # print(graph_algo.shortest_path(21, 7))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(23))

    def test_a5(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A5")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(47, 4))
        # print(graph_algo.shortest_path(37, 20))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(22))

    def test_a5_edited(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/A5_edited")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(47, 4))
        # print(graph_algo.shortest_path(37, 20))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(0))

    def test_T0(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/T0.json")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(0, 2))
        # print(graph_algo.shortest_path(3, 1))
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(1))

    def test_random_graph(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/Random_graph.json")
        # graph_algo.plot_graph()
        # print(graph_algo.shortest_path(11, 5300))
        # print(graph_algo.shortest_path(700, 2300))
        # print(graph_algo.shortest_path(9000, 233))
        # print(graph_algo.connected_components())

    def test_random_graph2(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/Random_graph2.json")
        # graph_algo.plot_graph()
        # print(graph_algo.connected_components())
        print(graph_algo.connected_component(44))

    def test_huge_random_graph(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../data/huge_random_graph.json")
        # graph_algo.plot_graph()
        print(graph_algo.shortest_path(8211, 23003))
