from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.utilities.Jsonconverter import json_to_graph

class TestGraphAlgo(TestCase):


    def test_shortest_path(self):
        # graphalgo = GraphAlgo.load_from_json()
        graph = json_to_graph("../data/Random_graph.json")
        graphalgo = GraphAlgo(graph)
        print(graphalgo.shortest_path(1, 8))

