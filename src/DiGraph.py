from GraphInterface import GraphInterface
from node_data import node_data

class DiGraph(GraphInterface):
    def __init__(self):
        self.N = {}
        self.E = {}
        self.RE = {}
        self.MC = 0
        self.edge_size = 0

    def copy(self):
        pass

    def v_size(self) -> int:
        return len(self.N)

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not (id1 in self.N.keys() and id2 in self.N.keys()):
            return False
        if id2 in self.E[id1].keys():
            if self.E[id1][id2] == weight:
                return False
            self.E[id1][id2] = weight
            self.RE[id2][id1] = weight
            self.MC += 1
            return True
        self.E[id1][id2] = weight
        self.RE[id2][id1] = weight
        self.MC += 1
        self.edge_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.N.keys():
            return False
        self.N[node_id] = node_data(node_id)
        self.E[node_id] = {}
        self.RE[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.N.keys():
            return False
        for key in self.RE.keys():
            self.E[key].pop(node_id)
            self.edge_size -= 1
            self.MC += 1
        self.E.pop(node_id)
        self.RE.pop(node_id)
        self.N.pop(node_id)
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not (node_id1 in self.N.keys() and node_id2 in self.N.keys()):
            return
        if node_id2 in self.E[node_id1].keys():
            self.E[node_id1].pop(node_id2)
            self.RE[node_id2].pop(node_id1)
            self.edge_size -= 1
            self.MC += 1

    def get_all_v(self) -> dict:
        return self.N

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.RE[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.E[id1]

    
