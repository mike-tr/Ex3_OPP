from src.DiGraph import DiGraph as _DiGraph
from src.NodeData import NodeData as _Node
from src.utilities.Vector3 import Vector3 as _Vec3
import random as _rand


def update_bounds(min_bound: _Vec3, max_bound: _Vec3, target: _Vec3):
    if target.x > max_bound.x:
        max_bound.x = target.x
    if target.x < min_bound.x:
        min_bound.x = target.x

    if target.y > max_bound.y:
        max_bound.y = target.y
    if target.y < min_bound.y:
        min_bound.y = target.y


def create_default_positions(graph: _DiGraph) -> (_Vec3, _Vec3):
    min_bound = _Vec3(float("-inf"), float("-inf"), 0)
    max_bound = _Vec3(float("inf"), float("inf"), 0)

    non_pos_nodes = []

    node: _Node
    for node in graph.get_all_v().values():
        if node.pos is not None:
            update_bounds(min_bound, max_bound, node.pos)
        else:
            non_pos_nodes.append(node)

    if min_bound.x == max_bound.x:
        min_bound.x -= 0.5
        max_bound.x += 0.5

    if min_bound.y == max_bound.y:
        min_bound.y -= 0.5
        max_bound.y += 0.5

    if min_bound.y == float("-inf"):
        min_bound = _Vec3(0, 0, 0)
        max_bound = _Vec3(1, 1, 0)

    node: _Node
    _rand.seed(42)

    scale = max_bound - min_bound
    for node in non_pos_nodes:
        node.default_pos = _Vec3(_rand.random() * scale.x, _rand.random() * scale.y, 0)
        node.default_pos += min_bound
