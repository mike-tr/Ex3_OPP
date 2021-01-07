class node_data:


    def __init__(self, key: int):
        self._key = key
        self._tag = tag = 0
        self._weight = 0
        self._pos = (0, 0, 0)

    def getkey(self) -> int:
        return self._key

    def gettag(self):
        return self._tag

    def getweight(self):
        return self._weight

    def getpos(self):
        return self._pos

    def settag(self, tag):
        self._tag = tag

    def setweight(self, weight):
        self._weight = weight

    def setpos(self, x: float, y: float, z: float):
        self._pos[0] = x
        self._pos[1] = y
        self._pos[2] = z

    def __repr__(self):
        return "node_data: { Key: " + str(self._key) + " }"

    def __eq__(self, other):
        if isinstance(other, node_data):
            if other.getkey() == self._key:
                return True
        return False