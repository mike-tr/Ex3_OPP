from unittest import TestCase as Tester
from src.DiGraph import DiGraph
from Tests.dummyGraph import graph_creator
from src.GraphAlgo import GraphAlgo
from src.utilities.Vector3 import Vector3
from src.NodeData import NodeData

import time

graph: DiGraph = None
v = 1000
e = v * 50

path = "../MyGraph"
save = e < 5000001


def test_load():
    if not save:
        return
    algo = GraphAlgo()
    algo.load_from_json(path)


# noinspection PyMethodMayBeStatic
class MyTestCase(Tester):

    def test_creation(self):
        global graph
        graph = graph_creator(v, e)
        node: NodeData
        for node in graph.get_all_v().values():
            node.pos = Vector3(0, 0, 0)

    def test_save(self):
        if not save:
            return
        algo = GraphAlgo(graph)
        print(graph)
        algo.save_to_json(path)


if __name__ == '__main__':
    Tester.main()
