from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.utilities.GraphDrawer import plot_graph


class Test(TestCase):
    def test_draw(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/A0")
        graph = ga.get_graph()
        plot_graph(graph)
