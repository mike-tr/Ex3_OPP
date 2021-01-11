from src.DiGraph import DiGraph
from src.NodeData import NodeData
from collections import deque

FRESH = 0
SEEN = 1
MARKED = 2


class _BfsNode(NodeData):
    def __init__(self):
        self.bfs_color = FRESH
        self.bfs_index = -1

    def add_fields(self, parent: __init__):
        self.bfs_color = FRESH
        self.bfs_index = -1

    def remove_fields(self):
        delattr(self, "bfs_color")
        delattr(self, "bfs_index")

    def is_dist_node(self):
        return hasattr(self, "bfs_index")


# noinspection PyTypeChecker
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

        for node_id in self._graph.get_all_v():
            vertex: _BfsNode = self._graph.get_node(node_id)
            vertex.bfs_color = FRESH

        self.components = []
        for node_id in self._graph.get_all_v():
            node: _BfsNode = self._graph.get_node(node_id)
            if node.bfs_index == -1:
                self._bfs_visit(node)
                self.components.append(self.component)

    def _bfs_visit(self, node: _BfsNode):
        # print("----------", node.get_key(), "-------------")
        self.component = []
        node.bfs_index = node.get_key()
        node.bfs_color = MARKED

        # arr = [node]
        stack = deque()
        stack2 = deque()

        stack.append(node)
        while stack:
            current: _BfsNode = stack.pop()
            stack2.append(current)

            for neighbour_id in self._graph.all_out_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_index == -1 and neighbour.bfs_color is FRESH:
                    neighbour.bfs_color = SEEN
                    stack.append(neighbour)

        stack = deque()
        stack.append(node)
        while stack:
            current: _BfsNode = stack.pop()

            self.component.append(current.get_key())
            current.bfs_index = node.bfs_index

            for neighbour_id in self._graph.all_in_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_color is SEEN:
                    neighbour.bfs_color = MARKED
                    stack.append(neighbour)

        while stack2:
            forget: _BfsNode = stack2.pop()
            forget.bfs_color = FRESH
