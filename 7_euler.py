import matplotlib.pyplot as plt
import networkx as nx
from random import choice
from colorization import *

my_graph = nx.Graph()
input = open('input_euler.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph.add_edge(start, end, weight=int(current_weight))

euler = nx.is_eulerian(my_graph)
print('Эйлеров?:', euler)
if euler:
    euler_cycle = nx.eulerian_circuit(my_graph)
    labels = {node: node for node in euler_cycle}
    edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True) if (start, end) in labels or (
    end, start) in labels]
    my_graph = nx.Graph()
    my_graph.add_edges_from(edges)
    positions = nx.spring_layout(my_graph)

    nx.draw_networkx_nodes(my_graph, positions, node_size=500, node_color=colorize())
    nx.draw_networkx_labels(my_graph, positions, font_size=12, font_family='sans-serif', font_color=colorize())
    nx.draw_networkx_edges(my_graph, positions, edgelist=my_graph.edges(), width=6)

    plt.axis('off')
    plt.savefig("weighted_graph.png")
    plt.show()
