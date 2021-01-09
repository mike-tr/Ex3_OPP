from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from src.NodeData import NodeData
import matplotlib.pyplot as plt
from src.utilities.DrawerUtil import create_default_positions
from src.utilities.Vector3 import Vector3


def draw(graph: DiGraph):
    bounds = create_default_positions(graph)
    scale: Vector3 = bounds[1] - bounds[0]

    print(bounds)

    nodes = graph.get_all_v().values()
    node: NodeData

    for node in nodes:
        pos = node.get_draw_pos()

        # plt.Circle(())
        plt.scatter(pos.x, pos.y, s=100, color='r')
        plt.text(pos.x + scale.x * 0.02, pos.y + scale.y * 0.06, str(node.get_key()))
        edges: dict
        for edge in graph.all_out_edges_of_node(node.get_key()).keys():
            other_pos = graph.get_node(edge).get_draw_pos()
            direction = (other_pos - pos)
            start = pos
            direction = direction * 0.9

            plt.arrow(start.x, start.y, direction.x, direction.y, width=0.00001, head_width=scale.x * 0.015)
    plt.show()
