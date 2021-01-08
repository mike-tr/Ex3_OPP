from typing import List

from src import GraphAlgoInterface
from src import GraphInterface
from src import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        if graph is None:
            graph = DiGraph()
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def load_from_json(self, file_name: str) -> bool:
        pass
