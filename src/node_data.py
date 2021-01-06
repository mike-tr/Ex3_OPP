class node_data:


    def __init__(self, key):
        self.__key = key
        self.tag = tag = 0
        self.weight = 0
        self.pos = (0, 0, 0)

    def GetKey(self):
        return self.__key