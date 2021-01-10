from src.DiGraph import DiGraph as _DiGraph
from src.NodeData import NodeData as _NodeData
import json as _json
import networkx as nx


# Checks if node has pos
def check_type(graph: _DiGraph) -> bool:
    node: _NodeData
    for node in graph.get_all_v().values():
        return node.pos is None


def graph_to_json(graph: _DiGraph) -> dict:
    dic = {}
    t = check_type(graph)
    nodes_arr = []
    edges_arr = []
    node: _NodeData
    for node in graph.get_all_v().values():
        if node.pos is None:
            nodes_arr.append({"id": node.get_key()})
        else:
            pos = node.pos
            p = str(float(pos.x)) + "," + str(float(pos.y)) + "," + str(float(pos.z))
            nodes_arr.append({"id": node.get_key(), "pos": p})
        for edge in graph.all_out_edges_of_node(node.get_key()).items():
            dic2 = {"src": node.get_key(), "dest": edge[0], "w": edge[1]}
            edges_arr.append(dic2)
    dic["Nodes"] = nodes_arr
    dic["Edges"] = edges_arr
    return dic


def save_graph(graph: _DiGraph, file: str):
    dic = graph_to_json(graph)
    with open(file, 'w') as f:
        _json.dump(dic, f)
        f.close()


def load_graph(file: str) -> _DiGraph:
    with open(file) as f:
        json_string = _json.load(f)
        f.close()
    graph = _DiGraph()
    dic = dict(json_string)
    nodes = dic['Nodes']
    node: dict
    for node in nodes:
        pos: object = None
        if "pos" in node:
            pos: str = node['pos']
            pos: list = pos.split(',')
            pos: tuple = tuple(map(float, pos))
        graph.add_node(node['id'], pos)
    for edge in dic['Edges']:
        graph.add_edge(edge['src'], edge['dest'], edge['w'])
    return graph


def load_networkx_graph(file: str) -> nx.Graph:
    with open(file) as f:
        json_string = _json.load(f)
        f.close()
    graph = nx.Graph()
    dic = dict(json_string)
    nodes = dic['Nodes']
    node: dict
    for node in nodes:
        pos: object = None
        if "pos" in node:
            pos: str = node['pos']
            pos: list = pos.split(',')
            pos: tuple = tuple(map(float, pos))
        graph.add_node(node['id'])
        graph.nodes[node['id']]['pos'] = pos
    for edge in dic['Edges']:
        graph.add_edge(edge['src'], edge['dest'], weight=edge['w'])
    return graph
