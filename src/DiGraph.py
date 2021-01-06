from GraphInterface import GraphInterface
from node_data import node_data

class DiGraph(GraphInterface):
    def __init__(self):
        self.__Nodes = {}
        self.__Edges = {}
        self.__Backward_Edges = {}
        self.MC = 0
        self.edge_size = 0

    def copy(self):
        pass

    def v_size(self) -> int:
        return len(self.__Nodes)

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not (id1 in self.__Nodes.keys() and id2 in self.__Nodes.keys()):
            return False
        if id2 in self.__Edges[id1].keys():
            if self.__Edges[id1][id2] == weight:
                return False
            self.__Edges[id1][id2] = weight
            self.__Backward_Edges[id2][id1] = weight
            self.MC += 1
            return True
        self.__Edges[id1][id2] = weight
        self.__Backward_Edges[id2][id1] = weight
        self.MC += 1
        self.edge_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.__Nodes.keys():
            return False
        self.__Nodes[node_id] = node_data(node_id)
        self.__Edges[node_id] = {}
        self.__Backward_Edges[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.__Nodes.keys():
            return False
        for key in self.__Backward_Edges[node_id].keys():
            self.__Edges[key].pop(node_id)
            self.edge_size -= 1
            self.MC += 1
        self.__Edges.pop(node_id)
        self.__Backward_Edges.pop(node_id)
        self.__Nodes.pop(node_id)
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not (node_id1 in self.__Nodes.keys() and node_id2 in self.__Nodes.keys()):
            return
        if node_id2 in self.__Edges[node_id1].keys():
            self.__Edges[node_id1].pop(node_id2)
            self.__Backward_Edges[node_id2].pop(node_id1)
            self.edge_size -= 1
            self.MC += 1

    def get_all_v(self) -> dict:
        return self.__Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__Backward_Edges[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__Edges[id1]


