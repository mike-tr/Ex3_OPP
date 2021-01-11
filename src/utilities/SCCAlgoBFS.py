from src.DiGraph import DiGraph
from src.NodeData import NodeData
from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2

NO_SCC = -1


class _BfsNode(NodeData):
    def __init__(self):
        self.bfs_color = WHITE
        self.bfs_index = -1

    def add_fields(self, parent: __init__):
        self.bfs_color = WHITE
        self.bfs_index = -1

    def remove_fields(self):
        delattr(self, "bfs_color")
        delattr(self, "bfs_index")

    def is_dist_node(self):
        return hasattr(self, "bfs_index")


class SCCAlgoBFS:
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
        self._bfs_forward()

        for node_id in self._graph.get_all_v():
            node = self._graph.get_node(node_id)
            _BfsNode.remove_fields(node)
        return self.components

    def _bfs_forward(self):
        for node_id in self._graph.get_all_v():
            node = self._graph.get_node(node_id)
            _BfsNode.add_fields(node, None)

        self.components = []
        for node_id in self._graph.get_all_v():
            node: _BfsNode = self._graph.get_node(node_id)
            if node.bfs_index is NO_SCC:
                self._bfs_visit(node)
                self.components.append(self._component)

    def _bfs_visit(self, node: _BfsNode):
        # print("----------", node.get_key(), "-------------")
        self._component = []
        node.bfs_index = node.get_key()
        node.bfs_color = BLACK

        # arr = [node]
        stack = deque()
        stack2 = deque()

        stack.append(node)
        while stack:
            current: _BfsNode = stack.pop()
            stack2.append(current)

            for neighbour_id in self._graph.all_out_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_index is NO_SCC and neighbour.bfs_color is WHITE:
                    neighbour.bfs_color = GRAY
                    stack.append(neighbour)

        stack = deque()
        stack.append(node)
        while stack:
            current: _BfsNode = stack.pop()

            self._component.append(current.get_key())
            current.bfs_index = node.bfs_index

            for neighbour_id in self._graph.all_in_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_color is GRAY:
                    neighbour.bfs_color = BLACK
                    stack.append(neighbour)

        while stack2:
            forget: _BfsNode = stack2.pop()
            forget.bfs_color = WHITE
