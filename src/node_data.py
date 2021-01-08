class node_data:


    def __init__(self, key: int):
        self._key = key
        self._tag = tag = 0
        self._weight = 0
        self._pos = (0, 0, 0)

    def get_key(self) -> int:
        return self._key

    def get_tag(self):
        return self._tag

    def get_weight(self):
        return self._weight

    def get_pos(self):
        return self._pos

    def set_tag(self, tag):
        self._tag = tag

    def set_weight(self, weight):
        self._weight = weight

    def setpos(self, x: float, y: float, z: float):
        self._pos[0] = x
        self._pos[1] = y
        self._pos[2] = z

    def __repr__(self):
        return "node_data: { Key: " + str(self._key) + " }"

    def __eq__(self, other):
        if isinstance(other, node_data):
            if other.get_key() == self._key:
                return True
        return False