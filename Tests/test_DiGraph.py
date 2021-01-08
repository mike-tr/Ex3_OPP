from unittest import TestCase
from src.DiGraph import DiGraph

class TestDiGraph(TestCase):
    def test_add_nodes_edges(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        TestCase.assertEqual(self,10,graph.v_size())



