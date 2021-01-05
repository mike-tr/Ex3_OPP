from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.N = {}
        self.E = {}
        self.RE = {}


    def v_size(self) -> int:
        return len(N)

    def e_size(self) -> int:
        pass

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass