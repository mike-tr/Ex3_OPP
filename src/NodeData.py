from src.utilities.Vector3 import Vector3


class NodeData:
    def __init__(self, key: int, pos: tuple = None):
        self._key = key
        if pos is not None:
            self.pos: Vector3 = Vector3(pos[0], pos[1], pos[2])
        else:
            self.pos: Vector3 = None
            self.default_pos = Vector3(0, 0, 0)

    def get_key(self) -> int:
        return self._key

    def get_pos(self):
        return self.pos

    def get_draw_pos(self) -> Vector3:
        if self.pos is None:
            return self.default_pos
        return self.pos

    def __repr__(self):
        return "node_data: { Key: " + str(self._key) + " }"

    def __eq__(self, other):
        if isinstance(other, NodeData):
            if other.get_key() == self._key:
                return True
        return False
