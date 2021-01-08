import unittest
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):
    def test_something(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)

        for i in range(9):
            graph.add_edge(i, i + 1, 1)

        print(graph._Edges[0])
        print(graph._Edges[0].items())
        g = GraphAlgo(graph)

        print(g.shortest_path(1, 2))


if __name__ == '__main__':
    unittest.main()
