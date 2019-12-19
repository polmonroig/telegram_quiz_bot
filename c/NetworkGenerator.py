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

    def add_node_with_content(self, node, content):
        self.graph.add_node(str(node), content=content)

    def add_node(self, node):
        self.graph.add_node(str(node))


    def add_item_edge(self, a, b, label):
        self.item_edges.append((a, b))
        self.graph.add_edge(str(a), str(b))
        self.labels[(a, b)] = label

    def add_alt_edge(self, a, b, label):
        self.alt_edges.append((a, b))
        self.graph.add_edge(str(a), str(b),  content=label)
        self.labels[(a, b)] = label

    def add_poll_edge(self, a, b):
        self.poll_edges.append((a, b))
        self.graph.add_edge(str(a), str(b))

    """
    Given a node P of a poll the ordering is 
    [Pi, Ri, Ai, .., An]
    if P is a final node, meaning that is the last question then 
    Pi = END 
    
    Given a node P that is not in a poll then the ordering is 
    [Ri, Ai, .., An]
    
    """
    def draw(self):
        node = 'E'
        succesors = list(self.graph.successors(node))
        while succesors:
            if node != 'E':
                print("Question:", self.graph.nodes[node]['content'])
                print("Answers:")
                for i, answer in enumerate(self.graph.nodes[succesors[1]]['content']):
                    print(str(i) + ":",answer)

            node = succesors[0]
            succesors = list(self.graph.successors(node))

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
        pickle.dump(self.graph, open("graph.p", "wb"))
