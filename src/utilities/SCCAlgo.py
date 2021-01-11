from src.DiGraph import DiGraph
from src.NodeData import NodeData

WHITE = 0
GRAY = 1
BLACK = 2


class _DfsNode(NodeData):
    def __init__(self):
        self.dfs_parent: _DfsNode = None
        self.dfs_color = WHITE

    def add_fields(self, parent: __init__):
        self.dfs_parent = parent
        self.dfs_color = WHITE

    def remove_fields(self):
        delattr(self, "dfs_parent")
        delattr(self, "dfs_color")

    def is_dist_node(self):
        return hasattr(self, "dfs_parent")


# noinspection PyTypeChecker
class SCCAlgo:
    """
    this class is responsible for generating Strongly connected components of a given graph
    """

    def __init__(self):
        self._graph = None
        self._dag = []
        self._component = []
        self.components = []

    def calculate_scc(self, graph: DiGraph) -> list:
        """this method will generate the a list of all strongly connected components"""
        if not isinstance(graph, DiGraph):
            return
        self._graph = graph
        self._dfs_forward()
        self._dfs_backwards()

        for node_id in self._graph.get_all_v():
            node = self._graph.get_node(node_id)
            _DfsNode.remove_fields(node)
        return self.components

    def _dfs_backwards(self):
        self.components = []
        self._component = []
        node: _DfsNode
        for node in self._dag:
            node.dfs_color = WHITE

        for node in self._dag:
            if node.dfs_color is WHITE:
                self._dfs_component(node)
                self.components.append(self._component)
                self._component = []

    def _dfs_component(self, node: _DfsNode):
        node.dfs_color = GRAY
        self._component.append(node.get_key())

        for neighbour_id in self._graph.all_in_edges_of_node(node.get_key()).keys():
            neighbour: _DfsNode = self._graph.get_node(neighbour_id)
            if neighbour.dfs_color is WHITE:
                self._dfs_component(neighbour)

    def _dfs_forward(self):
        for node_id in self._graph.get_all_v():
            node = self._graph.get_node(node_id)
            _DfsNode.add_fields(node, None)

        for node_id in self._graph.get_all_v():
            node: _DfsNode = self._graph.get_node(node_id)
            if node.dfs_color is WHITE:
                self._dfs_visit(node)

    def _dfs_visit(self, node: _DfsNode):
        node.dfs_color = GRAY
        for neighbour_id in self._graph.all_out_edges_of_node(node.get_key()).keys():
            neighbour: _DfsNode = self._graph.get_node(neighbour_id)
            if neighbour.dfs_color is WHITE:
                neighbour.dfs_parent = node
                self._dfs_visit(neighbour)

        node.dfs_color = BLACK
        self._dag.insert(0, node)
