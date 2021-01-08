from unittest import TestCase
from src.DiGraph import DiGraph
import random


def graph_gen(v_size: int, e_size: int) -> DiGraph:
    graph = DiGraph()
    for i in range(v_size):
        graph.add_node(i)
    random.seed(42)
    a = random.randint(0, v_size)
    b = random.randint(0, v_size)
    w = random.uniform(0.1, 10)
    graph.add_edge(a, b, w)
    return graph


class TestDiGraph(TestCase):

    def test_runtime(self):
        graph = graph_gen(100000, 1000000)

    def test_add_nodes(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        TestCase.assertEqual(self, 10, graph.v_size())
        graph.add_node(5)
        TestCase.assertEquals(self, 10, graph.v_size())

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(6):
            graph.add_node(i)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 1, 3)
        TestCase.assertEqual(self, 5, graph.get_edge(0, 1))
        TestCase.assertEqual(self, -1, graph.get_edge(1, 0))
        TestCase.assertEqual(self, 1, graph.e_size())
        graph.add_edge(0, 2, 3)
        TestCase.assertEqual(self, 2, graph.e_size())
        graph.add_edge(0, 3, 3)
        TestCase.assertEqual(self, 3, graph.get_edge(0, 3))
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 10, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 2)
        TestCase.assertEqual(self, 2, graph.get_edge(0, 3))
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