from unittest import TestCase as Tester
from Tests.dummyGraph import graph_creator
from src.utilities.SCCAlgo import SCCAlgo


class TestSCCAlgo(Tester):
    def test_size(self):
        v = 1000
        graph = graph_creator(v, v * 2)
        scc_bfs = SCCAlgo()

        scc_bfs.calculate_scc(graph)

    def test_strongly_connected(self):
        graph = graph_creator(100)
        for i in range(1, 100):
            graph.add_edge(i - 1, i, 1)
        scc_algo = SCCAlgo()
        scc_algo.calculate_scc(graph)
        Tester.assertEqual(self, len(scc_algo.components), 100)

        graph.add_edge(99, 0, 1)
        scc_algo.calculate_scc(graph)
        Tester.assertEqual(self, len(scc_algo.components), 1)

    def test_scc(self):
        graph = graph_creator(8)
        graph.add_edge(0, 1, 0.5)
        graph.add_edge(1, 2, 0.5)
        graph.add_edge(2, 0, 0.5)

        graph.add_edge(3, 4, 0.5)
        graph.add_edge(4, 3, 0.5)

        graph.add_edge(6, 7, 0.5)
        graph.add_edge(7, 6, 0.5)

        graph.add_edge(1, 3, 5.1)
        graph.add_edge(3, 6, 5.5)
        graph.add_edge(1, 7, 5.5)
        graph.add_edge(2, 7, 5.5)
        graph.add_edge(6, 5, 3.3)
        graph.add_edge(4, 5, 3.3)

        scc_algo = SCCAlgo()
        print(scc_algo.calculate_scc(graph))

        scc_components = []
        scc: list
        for scc in scc_algo.components:
            scc_components.append(sorted(scc))

        scc1 = [0, 1, 2]
        scc2 = [3, 4]
        scc3 = [5]
        scc4 = [6, 7]
        Tester.assertTrue(self, scc_components.__contains__(scc1))
        Tester.assertTrue(self, scc_components.__contains__(scc2))
        Tester.assertTrue(self, scc_components.__contains__(scc3))
        Tester.assertTrue(self, scc_components.__contains__(scc4))

        graph.add_edge(7, 2, 2.2)

        scc_components = []
        scc_algo.calculate_scc(graph)
        for scc in scc_algo.components:
            scc_components.append(sorted(scc))

        scc1 = [0, 1, 2, 3, 4, 6, 7]
        scc2 = [3, 4]
        scc3 = [5]
        print(scc_components)
        Tester.assertTrue(self, scc_components.__contains__(scc1))
        Tester.assertFalse(self, scc_components.__contains__(scc2))
        Tester.assertTrue(self, scc_components.__contains__(scc3))
        Tester.assertFalse(self, scc_components.__contains__(scc4))

        graph.remove_edge(3, 6)
        scc_components = []
        scc_algo.calculate_scc(graph)
        for scc in scc_algo.components:
            scc_components.append(sorted(scc))

        scc1 = [0, 1, 2, 6, 7]
        print(scc_components)
        Tester.assertTrue(self, scc_components.__contains__(scc1))
        Tester.assertTrue(self, scc_components.__contains__(scc2))
        Tester.assertTrue(self, scc_components.__contains__(scc3))
        Tester.assertFalse(self, scc_components.__contains__(scc4))


if __name__ == '__main__':
    Tester.main()
