from unittest import TestCase as Tester
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from Tests.dummyGraph import graph_creator


def dump(obj):
    print(obj.__dict__)


class TestGraphAlgo(Tester):
    def test_empty_graph(self):
        algo = GraphAlgo()
        path = algo.shortest_path(1, 2)
        Tester.assertEqual(self, path[1], [])
        Tester.assertEqual(self, path[0], float("inf"))
        Tester.assertEqual(self, algo.connected_components(), [])
        Tester.assertEqual(self, algo.connected_component(10), [])

    def test_scc(self):
        g = graph_creator(15)
        g.add_edge(9, 0, 2)
        for i in range(1, 10):
            g.add_edge(i - 1, i, 1)
        g.add_edge(10, 11, 3)
        g.add_edge(11, 12, 3)
        g.add_edge(12, 10, 2)

        algo = GraphAlgo(g)
        Tester.assertEqual(self, len(algo.connected_components()), 4)
        Tester.assertEqual(self, len(algo.connected_component(1)), len(algo.connected_component(2)))
        Tester.assertEqual(self, len(algo.connected_component(1)), 10)
        Tester.assertEqual(self, algo.connected_component(3), algo.connected_component(4))
        Tester.assertNotEqual(self, algo.connected_component(5), algo.connected_component(10))

        Tester.assertTrue(self, algo.connected_components().__contains__(algo.connected_component(0)))
        print(algo.connected_components())
        print(algo.connected_component(1))
        print(algo.connected_component(10))
        print(algo.connected_component(13))

    def test_path_to_self(self):
        g = graph_creator(10)
        algo = GraphAlgo(g)
        path = algo.shortest_path(0, 0)
        Tester.assertEqual(self, path[0], 0)
        print(path)
        for i in range(2):
            Tester.assertEqual(self, path[1][i], 0)

    def test_path_basic(self):
        g = graph_creator(100, 0)
        for i in range(1, 100):
            g.add_edge(i - 1, i, 10)
        algo = GraphAlgo(g)
        Tester.assertEqual(self, algo.shortest_path(0, 10)[0], 100)
        for i in range(1, 100):
            g.add_edge(i - 1, i, 1)
        Tester.assertEqual(self, algo.shortest_path(0, 10)[0], 10)

    def test_path(self):
        graph = DiGraph()
        for i in range(5 + 1):
            graph.add_node(i)
        graph.add_edge(1, 2, 10)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 100)
        graph.add_edge(2, 4, 5)
        graph.add_edge(2, 3, 50)
        graph.add_edge(3, 5, 30)
        graph.remove_edge(4, 5)

        g = GraphAlgo(graph)
        v = g.shortest_path(1, 5)
        Tester.assertEqual(self, 35, v[0])
        path = [1, 3, 5]
        for i in range(len(path)):
            Tester.assertEqual(self, path[i], v[1][i])

        graph.add_edge(4, 5, 10)
        v1 = g.shortest_path(1, 5)
        v2 = g.shortest_path(5, 1)

        Tester.assertEqual(self, 25, v1[0])
        Tester.assertEqual(self, float("inf"), v2[0])

        path = [1, 2, 4, 5]
        for i in range(len(path)):
            Tester.assertEqual(self, path[i], v1[1][i])

        graph.add_edge(4, 5, 100)
        v1 = g.shortest_path(1, 5)
        Tester.assertEqual(self, 35, v1[0])

    if __name__ == '__main__':
        Tester.main()
