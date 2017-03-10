import matplotlib.pyplot as plt
import networkx as nx
from colorization import *

my_graph = nx.Graph()
input = open('input.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph.add_edge(start, end, weight=int(current_weight))

for component in nx.connected_component_subgraphs(my_graph):
    positions = nx.spectral_layout(component)
    nx.draw_networkx_nodes(component, positions, node_size=500, node_color=colorize())
    nx.draw_networkx_labels(component, positions, font_size=12, font_family='sans-serif', font_color=colorize())
    nx.draw_networkx_edges(component, positions, edgelist=component.edges(), width=6)

plt.axis('off')
plt.savefig("weighted_graph.png")
plt.show()
