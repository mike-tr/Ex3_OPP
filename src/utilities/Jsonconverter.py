from src.DiGraph import DiGraph
from src.NodeData import NodeData
import json


# Checks if node has pos
def check_type(graph: DiGraph) -> bool:
    node: NodeData
    for node in graph.get_all_v().values():
        return node.pos == None


def Graph_to_Json(graph: DiGraph, file: str):
    dic = {}
    t = check_type(graph)
    nodes_arr = []
    edges_arr = []
    node: NodeData
    for node in graph.get_all_v().values():
        if t:
            nodes_arr.append({"id": node.get_key()})
        else:
            pos = node.pos
            p = str(pos.x) + "," + str(pos.y) + "," + str(pos.z)
            nodes_arr.append({"id": node.get_key(), "pos": p})
        for edge in graph.all_out_edges_of_node(node.get_key()).items():
            dic2 = {"src": node.get_key(), "dest": edge[0], "w": edge[1]}
            edges_arr.append(dic2)
    dic["Nodes"] = nodes_arr
    dic["Edges"] = edges_arr
    with open(file, 'w') as f:
        json.dump(dic, f)
        f.close()


def check_type_(nodes: list) -> bool:
    return "pos" in nodes[0].keys()


def Json_to_Graph(file: str) -> DiGraph:
    with open(file) as f:
        json_string = json.load(f)
        f.close
    graph = DiGraph()
    dic = dict(json_string)
    nodes = dic['Nodes']
    ty = check_type_(nodes)
    node: dict
    for node in nodes:
        if ty:
            pos: str
            pos = node['pos']
            pos = pos.split(',')
            pos: list
            pos = tuple(map(float, pos))
            graph.add_node(node['id'], pos)
        else:
            graph.add_node(node['id'])
    for edge in dic['Edges']:
        graph.add_edge(edge['src'], edge['dest'], edge['w'])
    return graph
