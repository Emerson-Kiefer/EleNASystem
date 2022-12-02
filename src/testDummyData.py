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

A = Node("A", 24.136472878664144, 49.22118714828496, 100, {})
B = Node("B", 24.137978719016566, 49.332132804948714, 50, {})
C = Node("C", 42.39, -72.53, 70, {})
D = Node("D", 42.35, -72.55, 40, {})
E = Node("E", 42.35, -72.52, 150, {})

A.addNeighbor(D, 100, 1000)
A.addNeighbor(E, 10, 100)

D.addNeighbor(A, 9, 99)

B.addNeighbor(A, 10, 17)

# B.getNeighbors().add(A)
# B.getNeighbors().add(C)
# B.getNeighbors().add(E)

# C.getNeighbors().add(B)
# C.getNeighbors().add(D)

# D.getNeighbors().add(A)
# D.getNeighbors().add(C)

# E.getNeighbors().add(A)
# E.getNeighbors().add(B)

# aToB = Edge(A, B, 100.0, 20.0)
# bToA = Edge(B, A, -100.0, 20.0)

# aToD = Edge(A, D, 250.0, 28.0)
# dToA = Edge(D, A, -250.0, 28.0)

# aToE = Edge(A, E, -50.0, 33.0)
# eToA = Edge(E, A, 50.0, 33.0)

dummyData.mapIdToNode("A", A)
dummyData.mapIdToNode("B", B)
dummyData.mapIdToNode("C", C)
dummyData.mapIdToNode("D", D)
dummyData.mapIdToNode("E", E)
print(dummyData.getNodeMap())

print(A)
print()
print(A.getNeighbors())

# print(dummyData.getNameNodeMap())
# print(dummyData.getNodeEdgeMap())

# print(A.getHaversineDistance(B))