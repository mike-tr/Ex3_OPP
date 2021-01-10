from unittest import TestCase as Tester
from src.utilities.Heap import Heap
from Tests.dummyGraph import graph_creator
from src.DiGraph import DiGraph
import random

import numpy


class Dummy:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __lt__(self, other):
        return self.val < other.val


class TestHeap(Tester):
    def test_runtime_graph(self):
        heap = Heap()
        random.seed(40)
        v = 10000
        graph = graph_creator(v, v * 10)
        for node in graph.get_all_v().values():
            heap.add_item(node, random.random() * 10)

        while heap.size() > 0:
            heap.pop_first()

    def test_runtime(self):
        heap = Heap()
        random.seed(40)

        for i in range(10000):
            # if i % 5 == 4:
            #     heap.pop_first()
            heap.add_item(Dummy(i), random.random() * 10)

        while heap.size() > 0:
            heap.pop_first()

    if __name__ == '__main__':
        Tester.main()
