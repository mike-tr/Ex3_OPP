from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from src.NodeData import NodeData
import matplotlib.pyplot as plt
from src.utilities.DrawerUtil import create_default_positions


def draw(graph: DiGraph):
    create_default_positions(graph)
    nodes = graph.get_all_v().values()
    node: NodeData
    for node in nodes:
        pos = node.get_draw_pos()
        plt.Circle(())
        # plt.scatter(pos.x, pos.y, s=100, color='r')
        plt.text(pos.x, pos.y, str(node.get_key()))
        edges: dict
        for edge in graph.all_out_edges_of_node(node.get_key()).keys():
            other_pos = graph.get_node(edge).get_draw_pos()
            vec = other_pos - pos
            plt.arrow(pos.x, pos.y,vec.x,vec.y, width = 0.00001, head_width=0.01 )
    plt.show()