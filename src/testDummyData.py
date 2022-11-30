import os
import sys
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../DS')
sys.path.insert(0, DS_path)

from Graph import Graph
from Node import Node
from Edge import Edge

dummyData = Graph()

A = Node("A", 42.37, -72.51, 100)
B = Node("B", 42.38, -72.50, 50)
C = Node("C", 42.39, -72.53, 70)
D = Node("D", 42.35, -72.55, 40)
E = Node("E", 42.35, -72.52, 150)

A.getNeighbors().add(B)
A.getNeighbors().add(D)
A.getNeighbors().add(E)

B.getNeighbors().add(A)
B.getNeighbors().add(C)
B.getNeighbors().add(E)

C.getNeighbors().add(B)
C.getNeighbors().add(D)

D.getNeighbors().add(A)
D.getNeighbors().add(C)

E.getNeighbors().add(A)
E.getNeighbors().add(B)

# aToB = Edge(A, B, 100.0, 20.0)
# bToA = Edge(B, A, -100.0, 20.0)

# aToD = Edge(A, D, 250.0, 28.0)
# dToA = Edge(D, A, -250.0, 28.0)

# aToE = Edge(A, E, -50.0, 33.0)
# eToA = Edge(E, A, 50.0, 33.0)

dummyData.mapStringToNode("A", A)
dummyData.mapStringToNode("B", B)
dummyData.mapStringToNode("C", C)
dummyData.mapStringToNode("D", D)
dummyData.mapStringToNode("E", E)
# dummyData.mapNodeToEdge(A, aToB)
# dummyData.mapNodeToEdge(A, aToD)
# dummyData.mapNodeToEdge(A, aToE)
print(A.getNeighbors())

print(dummyData.getNameNodeMap())
# print(dummyData.getNodeEdgeMap())