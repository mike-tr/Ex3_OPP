import unittest
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):
    def test_something(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        g = GraphAlgo(graph)

        g.shortest_path(0, 5)


if __name__ == '__main__':
    unittest.main()
