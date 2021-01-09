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
    fig, ax = plt.subplots()
    nodes = graph.get_all_v().values()
    node: NodeData

    ax: plt.Axes = plt.axes()
    for node in nodes:
        pos = node.get_draw_pos()
        # circle = plt.Circle((pos.x, pos.y), 0.5*plt.xscale(1), color='r')
        # ax.add_artist(circle)
        edges: dict
        for edge in graph.all_out_edges_of_node(node.get_key()).keys():
            other_pos = graph.get_node(edge).get_draw_pos()
            direction = (other_pos - pos)
            offset = direction.normalize() * scale.x * 0.02
            start = pos
            direction -= offset * 1
            ax.arrow(start.x, start.y, direction.x, direction.y,
                     width=0.001 * scale.x,
                     head_width=0.01 * scale.x,
                     head_length=0.02 * scale.x,
                     head_starts_at_zero=True,
                     length_includes_head=True,
                     fc='k',
                     ec='k')
        print(pos)
        plt.scatter(pos.x, pos.y, c='b')
        # ax.add_artist(plt.Circle(xy=pos.to_tuple2d(), radius=scale.x * 0.01))
        ax.text(pos.x + scale.x * 0.02, pos.y + scale.y * 0.03, str(node.get_key()))
    ax.set_aspect('equal', adjustable='datalim')
    plt.show()


if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("../../data/A5")
    graph = ga.get_graph()
    print(graph)
    draw(graph)
