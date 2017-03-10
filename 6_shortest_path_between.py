import matplotlib.pyplot as plt
import networkx as nx
from random import choice
from colorization import *

my_graph = nx.Graph()
input = open('input.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph.add_edge(start, end, weight=int(current_weight))

beginning = choice(my_graph.nodes())
paths = nx.shortest_path_length(my_graph, choice(my_graph.nodes()), weight='weight')
labels = {node: node + ': ' + str(paths[node]) for node in my_graph if node in paths}
labels.update({node: node + ': ' + str('+inf') for node in my_graph if node not in labels})
path_nodes = nx.shortest_path(my_graph, beginning, choice(list(paths.keys())), weight='weight')
positions = nx.spring_layout(my_graph)
edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True) if start not in path_nodes
         or end not in path_nodes]
color_edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True) if start in path_nodes
         and end in path_nodes]

nx.draw_networkx_nodes(my_graph, positions, node_size=500, node_color=colorize())
nx.draw_networkx_labels(my_graph, positions, labels, font_size=12, font_family='sans-serif', font_color=colorize())
nx.draw_networkx_edges(my_graph, positions, edgelist=edges, width=6)
nx.draw_networkx_edges(my_graph, positions, edgelist=color_edges, width=6, edge_color='red')

plt.axis('off')
plt.savefig("weighted_graph.png")
plt.show()
