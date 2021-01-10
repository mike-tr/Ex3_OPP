from src.DiGraph import DiGraph
from src.NodeData import NodeData

WHITE = 0
GRAY = 1
BLACK = 2


class _BfsNode(NodeData):
    def __init__(self):
        self.bfs_parent: _BfsNode = None
        self.bfs_color = WHITE
        self.bfs_index = -1

    def add_fields(self, parent: __init__):
        self.bfs_parent = parent
        self.bfs_color = WHITE
        self.bfs_index = -1

    def remove_fields(self):
        delattr(self, "bfs_parent")
        delattr(self, "bfs_color")
        delattr(self, "bfs_index")

    def is_dist_node(self):
        return hasattr(self, "dfs_parent")


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
        node.bfs_color = GRAY

        arr = [node]
        size = 1
        index = 0

        for node_id in self._graph.get_all_v():
            vertex: _BfsNode = self._graph.get_node(node_id)
            vertex.bfs_color = WHITE

        while index < size:
            current: _BfsNode = arr[index]
            self._dag.append(current)
            index += 1

            for neighbour_id in self._graph.all_out_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_index == -1 and neighbour.bfs_color is WHITE:
                    neighbour.bfs_color = GRAY
                    neighbour.bfs_parent = current
                    arr.append(neighbour)
                    size += 1

        arr = [node]
        size = 1
        index = 0
        while index < size:
            current: _BfsNode = arr[index]

            self.component.append(current.get_key())
            current.bfs_index = node.bfs_index
            index += 1

            for neighbour_id in self._graph.all_in_edges_of_node(current.get_key()).keys():
                neighbour: _BfsNode = self._graph.get_node(neighbour_id)
                if neighbour.bfs_color is GRAY:
                    neighbour.bfs_color = BLACK
                    arr.append(neighbour)
                    size += 1
