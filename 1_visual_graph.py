import matplotlib.pyplot as plt
import networkx as nx
from colorization import *

my_graph = nx.Graph()
input = open('input.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph.add_edge(start, end, weight=int(current_weight))
positions = nx.spring_layout(my_graph)
edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True)]

nx.draw_networkx_nodes(my_graph, positions, node_size=500, node_color=colorize())
nx.draw_networkx_labels(my_graph, positions, font_size=6, font_family='sans-serif', font_color=colorize())
nx.draw_networkx_edges(my_graph, positions, edgelist=edges, width=6)

plt.axis('off')
plt.savefig("weighted_graph.png")
plt.show()
