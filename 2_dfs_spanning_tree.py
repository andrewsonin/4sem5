import matplotlib.pyplot as plt
import networkx as nx
from random import choice
from colorization import *

my_graph = nx.Graph()
input = open('input.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph.add_edge(start, end, weight=int(current_weight))

spanning_tree = nx.dfs_tree(my_graph, source=choice(my_graph.nodes()))
positions = nx.spectral_layout(spanning_tree)

nx.draw_networkx_nodes(spanning_tree, positions, node_size=500, node_color=colorize())
nx.draw_networkx_labels(spanning_tree, positions, font_size=12, font_family='sans-serif', font_color=colorize())
nx.draw_networkx_edges(spanning_tree, positions, edgelist=spanning_tree.edges(), width=6)

plt.axis('off')
plt.savefig("weighted_graph.png")
plt.show()
