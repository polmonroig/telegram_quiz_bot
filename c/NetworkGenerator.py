import networkx as nx
import matplotlib.pyplot as plt


class NetworkGenerator:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def draw(self):
        options = {
            'node_color': '#91a8cc',
            'node_size': 500,
            'width': 3,
            'with_labels' : True
        }

        nx.draw(self.graph, **options)
        plt.savefig("path.png")
