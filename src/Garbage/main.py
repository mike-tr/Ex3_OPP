from src.NodeData import NodeData
import json


class TT:
    def __init__(self):
        self.x = 10
        self.name = "DEDED"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node = NodeData(10)

    k = TT()

    json_str = json.dumps(node.__dict__)
    print(json_str)
