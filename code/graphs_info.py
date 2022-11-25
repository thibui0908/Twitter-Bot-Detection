import csv
from math import degrees
from numpy import average
import pandas as pd
import networkx as nx
import os
import re

directory_edge = './data/real_user_edge'
directory_node = './data/real_user_nodes'

files_edge = [file for file in os.listdir(directory_edge)]
files_node = [file for file in os.listdir(directory_node)]

number_of_nodes = 0
number_of_edges = 0
number_isolated = 0
density = 0
max_degree = 0
min_degree = 0
average_degree = 0
connected_component = 0
count = 0

def social_network_analysis(edge_file, node_file):
    node_reader = csv.reader(node_file)
    node_list = list(node_reader)

    G = nx.Graph()

    for i in node_list:
        G.add_node(int(i[0]))

    edge_reader = csv.reader(edge_file)
    edge_list = list(edge_reader)

    for i in edge_list:
        G.add_edge(int(i[0]), int(i[1]))
    
    res = []

    res.append(G.number_of_nodes())
    res.append(G.number_of_edges())
    res.append(len(list(nx.isolates(G))))
    res.append(nx.density(G))
    degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)
    res.append(degrees[0][1])
    res.append(degrees[len(degrees)-1][1])

    sum = 0

    for i in degrees:
        sum = sum + i[1]
    
    res.append(sum/len(degrees))
    
    res.append(nx.number_connected_components(G))
    return res

def get_numbers_from_filename(filename):
    return re.search(r'\d+', filename).group(0)

for filename in files_edge:
    try:
        if os.path.getsize(os.path.join(directory_edge,filename)) > 0:
            with open(os.path.join(directory_edge, filename), 'r', encoding='utf-8') as openfile:
                filenum = get_numbers_from_filename(filename)
                with open(os.path.join(directory_node, 'real_user_nodes_{}.csv'.format(filenum)), 'r', encoding='utf-8') as nodefile:
                    count = count + 1
                    res = social_network_analysis(openfile, nodefile)
                    number_of_nodes = number_of_nodes + res[0]
                    number_of_edges = number_of_edges + res[1]
                    number_isolated = number_isolated + res[2]
                    density = density + res[3]
                    max_degree = max_degree + res[4]
                    min_degree = min_degree + res[5]
                    average_degree = average_degree + res[6]
                    connected_component = connected_component + res[7]
    except Exception as e:
        print("error:",e)

print("---------------------------------------------------------------------")
print("Number of nodes: ", number_of_nodes)
print("Average number of nodes: ", number_of_nodes/count)
print("Number of edges: ", number_of_edges)
print("Average number of edges: ", number_of_edges/count)
print("Number of isolated nodes", number_isolated/count)
print("Average density of a graph: ", density/count)

print("Average max degree: ", max_degree/count)
print("Average min degree: ", min_degree/count)
    
print("Average degree: ", average_degree/count)
print("Average number of connected components: ", connected_component/count)
print("---------------------------------------------------------------------")

