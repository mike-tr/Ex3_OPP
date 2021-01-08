from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        if graph is None:
            graph = DiGraph()
        elif not isinstance(graph, DiGraph):
            graph = DiGraph(graph)

    def get_graph(self) -> GraphInterface:
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        first = self.graph
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
