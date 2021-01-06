class node_data:


    def __init__(self, key):
        self.__key = key
        self.__tag = tag = 0
        self.__weight = 0
        self.__pos = (0, 0, 0)

    def getkey(self) -> int:
        return self.__key

    def gettag(self):
        return self.__tag

    def getweight(self):
        return self.__weight

    def getpos(self):
        return self.__pos

    def settag(self, tag):
        self.__tag = tag

    def setweight(self, weight):
        self.__weight = weight

    def __repr__(self):
        return "node_data: { Key: " + str(self.__key) + " }"

    def __eq__(self, other):
        if isinstance(other, node_data):
            if other.getkey() == self.__key:
                return True
        return False