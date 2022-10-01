import csv
from math import degrees
import pandas as pd
import networkx as nx

with open('./data/real_bot_user_nodes_0.csv', newline='') as f:
    reader = csv.reader(f)
    node_list = list(reader)

print(len(node_list))

G = nx.Graph()

for i in node_list:
    G.add_node(int(i[0]))


with open('./data/real_bot_user_edge_0.csv', newline='') as f:
    reader = csv.reader(f)
    edges = list(reader)

for i in edges:
    G.add_edge(int(i[0]), int(i[1]))

print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())
print("Number of isolated nodes", len(list(nx.isolates(G))))
print("Density of a graph: ", nx.density(G))

degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)

print("Max degree: ", degrees[0][1])
print("Min degree: ", degrees[len(degrees)-1][1])

sum = 0

for i in degrees:
    sum = sum + i[1]
    
print("Average degree: ", sum/len(degrees))
print("Number of connected components: ", nx.number_connected_components(G))
