from unittest import TestCase
from src.DiGraph import DiGraph
from Tests.dummyGraph import graph_creator
import random


# noinspection DuplicatedCode
class TestDiGraph(TestCase):
    graph: DiGraph = None

    def test_invalid_node(self):
        graph = graph_creator(10, 0)
        TestCase.assertEqual(self, {}, graph.all_in_edges_of_node(11))
        TestCase.assertEqual(self, False, graph.add_edge(0, 11, 2))

    def test_runtime(self):
        v = 100000
        e = v * 5
        TestDiGraph.graph = graph_creator(v, e)

    def test_copy(self):
        v = 10000
        e = v * 10
        graph = graph_creator(v, e)
        graph2 = DiGraph()
        graph2.copy(graph)
        TestCase.assertEqual(self, graph, graph2)
        graph.remove_node(0)
        self.assertNotEqual(graph, graph2)

    def test_add_nodes(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        TestCase.assertEqual(self, 10, graph.v_size())
        graph.add_node(5)
        TestCase.assertEqual(self, 10, graph.v_size())

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(6):
            graph.add_node(i)
        graph.add_edge(0, 1, 5)  # 1
        graph.add_edge(1, 1, 3)  # 1
        TestCase.assertEqual(self, 5, graph.get_edge(0, 1))
        TestCase.assertEqual(self, -1, graph.get_edge(1, 0))
        TestCase.assertEqual(self, 1, graph.e_size())
        graph.add_edge(0, 2, 3)  # 2
        TestCase.assertEqual(self, 2, graph.e_size())
        graph.add_edge(0, 3, 3)  # 3
        TestCase.assertEqual(self, 3, graph.get_edge(0, 3))
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 10, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 2)
        TestCase.assertEqual(self, 3, graph.get_edge(0, 3))
        TestCase.assertEqual(self, 3, graph.e_size())

    def test_remove_edge(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_edge(0, 1, 3)
        graph.add_edge(0, 2, 3)
        graph.add_edge(0, 3, 3)
        graph.add_edge(0, 4, 3)
        TestCase.assertEqual(self, 4, graph.e_size())
        graph.remove_edge(0, 4)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.remove_edge(0, 4)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.remove_edge(20, 30)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.remove_edge(0, 2)
        TestCase.assertEqual(self, 2, graph.e_size())

    def test_remove_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_edge(0, 1, 3)
        graph.add_edge(0, 2, 3)
        graph.add_edge(0, 3, 3)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 3)
        TestCase.assertEqual(self, 5, graph.e_size())
        graph.remove_node(0)
        TestCase.assertEqual(self, 0, graph.e_size())
        TestCase.assertEqual(self, 9, graph.v_size())
        graph.remove_node(0)
        TestCase.assertEqual(self, 0, graph.e_size())
        TestCase.assertEqual(self, 9, graph.v_size())

    def test_get_node(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        self.assertNotEqual(None, graph.get_node(0))
        self.assertNotEqual(None, graph.get_node(1))
        self.assertEqual(None, graph.get_node(-1))

    def test_get_edge(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(0, 1, 3)
        self.assertEqual(3, graph.get_edge(0, 1))
        self.assertEqual(-1, graph.get_edge(0, 2))
        self.assertEqual(-1, graph.get_edge(1, 0))
        self.assertEqual(-1, graph.get_edge(-1, 3))

    def test_v_size(self):
        graph = DiGraph()
        for i in range(20):
            graph.add_node(i)
        self.assertEqual(20, graph.v_size())
        for i in range(10, 20):
            graph.remove_node(i)
        self.assertEqual(10, graph.v_size())
        for i in range(10, 20):
            graph.remove_node(i)
        self.assertEqual(10, graph.v_size())
        for i in range(0, 10):
            graph.remove_node(i)
        self.assertEqual(0, graph.v_size())

    def test_e_size(self):
        graph = DiGraph()
        for i in range(20):
            graph.add_node(i)
        self.assertEqual(0, graph.e_size())
        graph.add_edge(1, 0, 1)
        self.assertEqual(1, graph.e_size())
        graph.add_edge(1, 0, 1)
        self.assertEqual(1, graph.e_size())
        graph.add_edge(1, 0, 2)
        self.assertEqual(1, graph.e_size())
        graph.add_edge(0, 1, 3)
        self.assertEqual(2, graph.e_size())
        graph.add_edge(0, 0, 1)
        self.assertEqual(2, graph.e_size())
        graph.add_edge(-1, 0, 1)
        self.assertEqual(2, graph.e_size())
        graph.add_edge(-1, 30, 1)
        self.assertEqual(2, graph.e_size())

    def test_get_all_v(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        nodes = graph.get_all_v()
        keys = nodes.keys()
        for i in range(10):
            self.assertTrue(i in keys)
        self.assertFalse(-1 in keys)
        self.assertEqual(10, len(keys))

    def test_all_out_edges(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(3, 7):
            graph.add_edge(0, i, 1)
        edges = graph.all_out_edges_of_node(0)
        self.assertEqual(4, len(edges))
        for i in range(-10, 3):
            self.assertFalse(i in edges.keys())
        for i in range(7, 100):
            self.assertFalse(i in edges.keys())
        for i in range(1, 10):
            self.assertEqual({}, graph.all_out_edges_of_node(i))

    def test_all_in_edges(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(3, 7):
            graph.add_edge(i, 0, 3)
        edges = graph.all_in_edges_of_node(0)
        self.assertEqual(4, len(edges))
        for i in range(-10, 3):
            self.assertFalse(i in edges.keys())
        for i in range(7, 100):
            self.assertFalse(i in edges.keys())
        for i in range(1, 10):
            self.assertEqual({}, graph.all_in_edges_of_node(i))

