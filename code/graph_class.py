import re
import csv
import os
import pandas as pd

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight = 0):
        self.connectedTo[neighbor] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
    
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numOfVertices = 0
    
    def addVertex(self, key):
        self.numOfVertices = self.numOfVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertexList
    
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertexList:
            nv = self.addVertex(f)
        if t not in self.vertexList:
            nv = self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], cost)
    
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())

#########

nodes = pd.read_csv('./data/bot_user_nodes/bot_user_nodes_357.csv', names = ['Id'],header=None)
nodes = nodes['Id']
num_nodes = nodes.shape[0]
print(num_nodes)
print(nodes)

edges = pd.read_csv('./data/bot_user_edge/bot_user_edge_357.csv',
                    names=['Source', 'Target'], header=None)
edges.shape
print(edges)

g = Graph()

for i in range(num_nodes):
  g.addVertex(nodes[i])

for i in range(len(edges)):
  edge = edges.iloc[i]
  g.addEdge(edge['Source'], edge['Target'])
  g.addEdge(edge['Target'], edge['Source'])

for v in g:
  for w in v.getConnections():
    print(" %s-%s" % (v.getId(), w.getId()))

from graphviz import Digraph

dot = Digraph(comment='connection-graph', format='png', strict = True)

for i in range(num_nodes):
  dot.node(str(nodes[i]))

print(edges)

for i in range(len(edges)):
  edge = edges.iloc[i]
  dot.edge(str(edge['Source']), str(edge['Target']))

print(dot.source)
dot.render('connection-graph.gv', view = True)

## Graph classification

graph_classification = {}
isBot = True
bot = 1
real = 2

graph_number = 1

graph_classification[bot] = []
graph_classification[real] = []
directories = ['./data/bot_user_edge/',
               './data/real_user_edge/']

bot_list = []
real_list = []

for directory in directories:
  isBot = True if directory == './data/bot_user_edge/' else False
  print('directory: ', directory, 'bot: ', isBot)
  for file in [file for file in os.listdir(directory) if file.endswith('.csv')]:
    with open(directory + file, 'r') as csv_file:
      edge_reader = csv.reader(csv_file)
      edge_list = list(edge_reader)
      if isBot:
        graph_classification[bot].append([graph_number, edge_list])
      else:
        graph_classification[real].append([graph_number, edge_list])
      graph_number += 1

print(graph_number)

for key in graph_classification.keys():
  if len(graph_classification[key]) == 0:
    graph_classification.pop(key)

#### Community detection



