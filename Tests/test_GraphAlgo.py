from unittest import TestCase as Tester
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from Tests.dummyGraph import graph_creator
from src.utilities import Jsonconverter as GJson

import json


def dump(obj):
    print(obj.__dict__)


# noinspection DuplicatedCode
class TestGraphAlgo(Tester):
    def test_plot_mixed(self):
        graph = graph_creator(100, 100)
        ga = GraphAlgo(graph)

        graph.add_node(200, (0, 0, 0))
        graph.add_node(201, (10, 5, 0))

        graph.add_edge(200, 201, 1)
        ga.plot_graph()

    def test_plot_random(self):
        graph = graph_creator(100, 100)
        ga = GraphAlgo(graph)

        ga.plot_graph()

    def test_plot(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/A0")
        ga.plot_graph()

    def test_load_save_fail(self):
        file = "../data/not_existing_file"
        algo = GraphAlgo()
        Tester.assertFalse(self, algo.load_from_json(file))

        algo._graph = None
        Tester.assertFalse(self, algo.save_to_json(file))

    def test_save_mixed(self):
        file = "../data/Test"

        graph = DiGraph()
        for i in range(3):
            graph.add_node(i, (i * i, i + 1.2, i + 2.1))
        graph.add_node(5)
        graph.add_node(6)
        graph.add_edge(1, 2, 3)
        graph.add_edge(1, 2, 4)
        graph.add_edge(1, 2, 3)
        graph.add_edge(1, 2, 4)

        algo = GraphAlgo(graph)
        algo.save_to_json(file)
        algo.load_from_json(file)

        compare1 = GJson.graph_to_json(graph)
        compare2 = GJson.graph_to_json(algo.get_graph())

        print(graph, "\n", algo.get_graph())
        print(compare1, "\n", compare2)

        Tester.assertEqual(self, compare1, compare2)
        Tester.assertNotEqual(self, str(graph), str(algo.get_graph()))

    def test_save_pos(self):
        file = "../data/Test"

        graph = DiGraph()
        for i in range(10):
            graph.add_node(i, (i * i, i + 1.2, i + 2))

        for i in range(1, 10):
            graph.add_edge(i - 1, i, i)

        algo = GraphAlgo(graph)
        algo.save_to_json(file)

        with open(file) as f:
            json_string = json.load(f)
            f.close()

        compare = GJson.graph_to_json(graph)
        Tester.assertEqual(self, compare, json_string)

        print(compare, "\n", json_string)

        graph.add_node(13)
        algo.save_to_json(file)

        with open(file) as f:
            json_string = json.load(f)
            f.close()

        compare = GJson.graph_to_json(graph)
        Tester.assertEqual(self, compare, json_string)
        print(compare, "\n", json_string)

    def test_save(self):
        file = "../data/Test"

        graph = graph_creator(100, 100)

        algo = GraphAlgo(graph)
        algo.save_to_json(file)

        with open(file) as f:
            json_string = json.load(f)
            f.close()

        compare = GJson.graph_to_json(algo.get_graph())
        Tester.assertEqual(self, compare, json_string)

        print(compare, "\n", json_string)

    def test_load(self):
        file = "../data/A0"

        json_string = ""
        with open(file) as f:
            json_string = json.load(f)
            f.close()

        algo = GraphAlgo()
        algo.load_from_json(file)

        compare = GJson.graph_to_json(algo.get_graph())
        Tester.assertEqual(self, compare, json_string)

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
