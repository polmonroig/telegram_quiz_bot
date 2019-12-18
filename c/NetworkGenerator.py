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

        # specifiy edge labels explicitly
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        nx.draw_networkx_nodes(self.graph, pos=pos)
        plt.savefig("path.png")
