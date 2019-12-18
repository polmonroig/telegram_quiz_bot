import networkx as nx
import matplotlib.pyplot as plt


class NetworkGenerator:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.NODE_COLOR = '#1f78b4'
        self.ITEM_COLOR = '#3838ff'

    def add_node(self, node):
        self.graph.add_node(str(node))

    def add_edge(self, a, b):

        self.graph.add_edge(str(a), str(b))

    def draw(self):
        options = {
            'node_color': self.NODE_COLOR,
            'node_size': 1000,
            'width': 2,
            'with_labels' : True,
            'edge_color' : self.ITEM_COLOR
        }
        # specifiy edge labels explicitly
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        nx.draw(self.graph, **options)
        plt.savefig("path.png")
