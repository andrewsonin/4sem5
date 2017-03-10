import matplotlib.pyplot as plt
import networkx as nx
from random import choice
from colorization import *

my_graph1 = nx.DiGraph()
my_graph = nx.Graph()
input = open('input_euler.txt', 'r', encoding='utf8')
for line in input:
    start, end, current_weight = line.strip().split()
    my_graph1.add_edges_from({(start, end), (end, start)})
    my_graph.add_edge(start, end)

cycles = list(nx.simple_cycles(my_graph1))
max_cycle = max(cycles, key=lambda x: len(x))
if len(max_cycle) == len(my_graph.nodes()):
    labels = {node: node for node in my_graph}
    labels.update({node: node + ': ' + str('+inf') for node in my_graph if node not in labels})
    positions = nx.spring_layout(my_graph)
    edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True) if start not in max_cycle
             or end not in max_cycle]
    color_edges = [(start, end) for (start, end, weight) in my_graph.edges(data=True) if start in max_cycle
                   and end in max_cycle]

    nx.draw_networkx_nodes(my_graph, positions, node_size=500, node_color=colorize())
    nx.draw_networkx_labels(my_graph, positions, labels, font_size=12, font_family='sans-serif', font_color=colorize())
    nx.draw_networkx_edges(my_graph, positions, edgelist=edges, width=6)
    nx.draw_networkx_edges(my_graph, positions, edgelist=color_edges, width=6, edge_color='red')

    plt.axis('off')
    plt.savefig("weighted_graph.png")
    plt.show()
else:
    print('Не гамильтонов')