from src.DiGraph import DiGraph
from src.NodeData import NodeData

WHITE = 0
GRAY = 1
BLACK = 2


class _DfsNode(NodeData):
    def __init__(self):
        self.dfs_parent: _DfsNode = None
        self.dfs_color = WHITE
        self.dfs_start_time = 0
        self.dfs_end_time = 0

    def add_fields(self, parent: __init__):
        self.dfs_parent = parent
        self.dfs_color = WHITE
        self.dfs_start_time = 0
        self.dfs_end_time = 0

    def remove_fields(self):
        delattr(self, "dfs_parent")
        delattr(self, "dfs_color")
        delattr(self, "dfs_start_time")
        delattr(self, "dfs_end_time")

    def is_dist_node(self):
        return hasattr(self, "dfs_parent")


# noinspection PyTypeChecker
class SCCAlgo:
    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.time = 0

    def dfs_visit(self, node: _DfsNode):
        node.dfs_color = GRAY
        self.time += 1
        node.dfs_start_time = self.time
        for neighbour_id in self.graph.all_out_edges_of_node(node.get_key()).keys():
            neighbour: _DfsNode = self.graph.get_node(neighbour_id)
            if neighbour.dfs_color is WHITE:
                neighbour.dfs_parent = node
                self.dfs_visit(neighbour)

        node.dfs_color = BLACK
        self.time += 1
        node.dfs_end_time = self.time

    def dfs_forward(self, start: int):
        for node_id in self.graph.get_all_v():
            node = self.graph.get_node(node_id)
            _DfsNode.add_fields(node, None)
        self.time = 0
        for node_id in self.graph.get_all_v():
            node: _DfsNode = self.graph.get_node(node_id)
            if node.dfs_color is WHITE:
                self.dfs_visit(node)
