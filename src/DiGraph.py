from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):
    def __init__(self):
        self._Nodes = {}
        self._Edges = {}
        self._Backward_Edges = {}
        self._MC = 0
        self._edge_size = 0

    def copy(self, other):
        if isinstance(other, GraphInterface):
            for node in other.get_all_v().keys():
                self.add_node(node)
            for node in other.get_all_v().keys():
                for edges in other.all_out_edges_of_node(node):
                    self.add_edge(node, edges[0], edges[1])

    def get_edge(self, node1: int, node2: int) -> (int, float):
        if node1 in self._Nodes and node2 in self._Nodes:
            if node2 in self._Edges[node1]:
                return self._Edges[node1][node2]
        return None

    def get_node(self, key: int) -> NodeData:
        if key in self._Nodes:
            return self._Nodes[key]

    def v_size(self) -> int:
        return len(self._Nodes)

    def e_size(self) -> int:
        return self._edge_size

    def get_mc(self) -> int:
        return self._MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        if weight < 0:
            return False
        if not (id1 in self._Nodes.keys() and id2 in self._Nodes.keys()):
            return False
        if id2 in self._Edges[id1].keys():
            if self._Edges[id1][id2][1] == weight:
                return False
            self._Edges[id1][id2] = (id2, weight)
            self._Backward_Edges[id2][id1] = (id1, weight)
            self._MC += 1
            return True
        self._Edges[id1][id2] = (id2, weight)
        self._Backward_Edges[id2][id1] = (id1, weight)
        self._MC += 1
        self._edge_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._Nodes.keys():
            return False
        self._Nodes[node_id] = NodeData(node_id)
        self._Edges[node_id] = {}
        self._Backward_Edges[node_id] = {}
        self._MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._Nodes.keys():
            return False
        for key in self._Backward_Edges[node_id].keys():
            self._Edges[key].pop(node_id)
            self._edge_size -= 1
            self._MC += 1
        self._edge_size -= len(self._Edges[node_id])
        self._Edges.pop(node_id)
        self._Backward_Edges.pop(node_id)
        self._Nodes.pop(node_id)
        self._MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not (node_id1 in self._Nodes.keys() and node_id2 in self._Nodes.keys()):
            return
        if node_id2 in self._Edges[node_id1].keys():
            self._Edges[node_id1].pop(node_id2)
            self._Backward_Edges[node_id2].pop(node_id1)
            self._edge_size -= 1
            self._MC += 1

    def get_all_v(self) -> dict:
        return self._Nodes

    """
    blablabal
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._Backward_Edges[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._Edges[id1]

    def __str__(self):
        return "DiGraph: { " + "Node size: " + str(len(self._Nodes)) + ", Edge size: " + str(
            self._edge_size) + ", MC: " + str(self._MC) + " }"

    def __eq__(self, other):
        if isinstance(other, GraphInterface):
            if other.get_all_v() == self._Nodes and other.e_size() == self._edge_size:
                for edge in other.get_all_v().keys():
                    if edge in self._Nodes and other.all_out_edges_of_node(edge) != self._Edges[edge]:
                        return False
                return True
        return False
