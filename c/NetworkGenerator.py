import networkx as nx
import matplotlib.pyplot as plt


class NetworkGenerator:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.NODE_COLOR = '#1f78b4'
        self.ITEM_COLOR = '#3838ff'
        self.ALT_COLOR = 'green'
        self.poll_edges = []
        self.item_edges = []
        self.alt_edges = []
        self.labels = {}

    def add_node(self, node):
        self.graph.add_node(str(node))

    def add_item_edge(self, a, b, label):
        self.item_edges.append((a, b))
        self.graph.add_edge(str(a), str(b))
        self.labels[(a, b)] = label

    def add_alt_edge(self, a, b, label):
        self.alt_edges.append((a, b))
        self.graph.add_edge(str(a), str(b))
        self.labels[(a, b)] = label

    def add_poll_edge(self, a, b):
        self.poll_edges.append((a, b))
        self.graph.add_edge(str(a), str(b))

    def draw(self):

        # specifiy edge labels explicitly
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos=pos, node_color=self.NODE_COLOR)
        nx.draw_networkx_labels(self.graph, pos=pos)
        nx.draw_networkx_edges(self.graph, pos=pos, edgelist=self.poll_edges)
        nx.draw_networkx_edges(self.graph, pos=pos, edgelist=self.item_edges, edge_color=self.ITEM_COLOR)
        nx.draw_networkx_edges(self.graph, pos=pos, edgelist=self.alt_edges, edge_color=self.ALT_COLOR)
        nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=self.labels)
        plt.savefig("path.png")
