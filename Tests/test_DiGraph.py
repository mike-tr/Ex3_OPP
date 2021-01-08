from unittest import TestCase
from src.DiGraph import DiGraph

class TestDiGraph(TestCase):
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
        TestCase.assertEqual(self, 5, graph.getedge(0, 1))
        TestCase.assertEqual(self, -1, graph.getedge(1, 0))
        TestCase.assertEqual(self, 1, graph.e_size())
        graph.add_edge(0, 2, 3)
        TestCase.assertEqual(self, 2, graph.e_size())
        graph.add_edge(0, 3, 3)
        TestCase.assertEqual(self, 3, graph.getedge(0, 3))
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 10, 3)
        TestCase.assertEqual(self, 3, graph.e_size())
        graph.add_edge(0, 3, 2)
        TestCase.assertEqual(self, 2, graph.getedge(0, 3))
        TestCase.assertEqual(self, 3, graph.e_size())

    def test_remove_edge(self):
        pass