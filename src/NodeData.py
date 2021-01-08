class NodeData:
    def __init__(self, key: int):
        self._key = key

    def get_key(self) -> int:
        return self._key

    def __repr__(self):
        return "node_data: { Key: " + str(self._key) + " }"

    def __eq__(self, other):
        if isinstance(other, NodeData):
            if other.get_key() == self._key:
                return True
        return False
