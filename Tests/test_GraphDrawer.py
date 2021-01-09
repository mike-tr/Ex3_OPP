from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.utilities.GraphDrawer import draw

class Test(TestCase):
    def test_draw(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/Test")
        graph = ga.get_graph()
        draw(graph)
