import networkx as nx
import matplotlib.pyplot as plt
import pickle


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

    def add_node_with_content(self, node, content, node_type):
        self.graph.add_node(str(node), content=content, in_poll=False, type=node_type)

    def add_node(self, node, node_type):
        self.graph.add_node(str(node), in_poll=False, type=node_type)

    def add_item_edge(self, a, b, label):
        self.item_edges.append((str(a), str(b)))
        self.graph.add_edge(str(a), str(b))
        self.labels[(str(a), str(b))] = str(label)

    def add_alt_edge(self, a, b, label):
        self.alt_edges.append((str(a), str(b)))
        self.graph.add_edge(str(a), str(b),  content=str(label))
        self.labels[(a, b)] = str(label)

    def add_poll_edge(self, a, b):
        self.poll_edges.append((str(a), str(b)))
        self.graph.add_edge(str(a), str(b))
        self.graph.nodes[str(a)]['in_poll'] = True
        self.graph.nodes[str(b)]['in_poll'] = True

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

    def save_graph(self):
        file = open("../bot/graph.p", "wb")
        pickle.dump(self.graph, file)
        file.close()
