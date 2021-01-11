from unittest import TestCase
from src.DiGraph import DiGraph
from Tests.dummyGraph import graph_creator
import random


# noinspection DuplicatedCode
class TestDiGraph(TestCase):
    graph: DiGraph = None

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
