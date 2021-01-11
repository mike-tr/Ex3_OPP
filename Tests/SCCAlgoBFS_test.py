from unittest import TestCase as Tester
from Tests.dummyGraph import graph_creator
from src.utilities.SCCAlgoBFS import SCCAlgoBFS
from src.utilities.SCCAlgo import SCCAlgo


# noinspection DuplicatedCode
class TestSCCAlgoBFS(Tester):
    def test_size(self):
        v = 1000
        graph = graph_creator(v, v * 2)
        scc_bfs = SCCAlgoBFS()

        scc_bfs.calculate_scc(graph)

    def test_compare_to_dfs(self):
        v = 1000
        graph = graph_creator(v, v * 2)
        scc_bfs = SCCAlgoBFS()
        scc_dfs = SCCAlgo()

        scc_components_bfs = []
        scc_bfs.calculate_scc(graph)

        size_bfs = 0
        for scc in scc_bfs.components:
            size_bfs += len(scc)
            scc_components_bfs.append(sorted(scc))

        scc_components_dfs = []
        scc_dfs.calculate_scc(graph)
        size_dfs = 0
        for scc in scc_dfs.components:
            size_dfs += len(scc)
            scc_components_dfs.append(sorted(scc))

        for scc in scc_components_dfs:
            Tester.assertTrue(self, scc_components_bfs.__contains__(scc))

    def test_strongly_connected(self):
        size = 10
        graph = graph_creator(size)
        graph.add_node(size)
        for i in range(1, size):
            graph.add_edge(i - 1, i, 1)
        scc_algo = SCCAlgoBFS()
        scc_algo.calculate_scc(graph)
        print(scc_algo.components)
        # Tester.assertEqual(self, len(scc_algo.components), 100)

        graph.add_edge(size - 1, 0, 1)
        scc_algo.calculate_scc(graph)
        print(scc_algo.components)
        # Tester.assertEqual(self, len(scc_algo.components), 1)

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

        scc_algo = SCCAlgoBFS()
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
