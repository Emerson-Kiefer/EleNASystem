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

S  = Node("S", 24, 49, 0, {})
A = Node("A", 24.10, 49.10, 0, {})
B = Node("B", 23.99, 49.01, 0, {})
C = Node("C", 24.00, 49.01, 0, {})
D = Node("D", 48, 48, 0, {})
G = Node("G", 24, 49.3, 0, {})

S.addNeighbor(A, S.getHaversineDistance(A), 0)
S.addNeighbor(B, S.getHaversineDistance(B), 0)
S.addNeighbor(C, S.getHaversineDistance(C), 0)
A.addNeighbor(S, A.getHaversineDistance(S), 0)
A.addNeighbor(B, A.getHaversineDistance(B), 0)
A.addNeighbor(G, A.getHaversineDistance(G), 0)
B.addNeighbor(S, B.getHaversineDistance(S), 0)
B.addNeighbor(A, B.getHaversineDistance(A), 0)
B.addNeighbor(D, B.getHaversineDistance(D), 0)
C.addNeighbor(S, C.getHaversineDistance(S), 0)
D.addNeighbor(B, D.getHaversineDistance(B), 0)
D.addNeighbor(G, D.getHaversineDistance(G), 0)
G.addNeighbor(A, G.getHaversineDistance(A), 0)
G.addNeighbor(D, G.getHaversineDistance(D), 0)







# A.addNeighbor(D, 100, 1000)
# A.addNeighbor(E, 10, 100)

# D.addNeighbor(A, 9, 99)

# B.addNeighbor(A, 10, 17)

# print(A)
# print()
# print(A.getNeighbors())

# print(dummyData.getNameNodeMap())
# print(dummyData.getNodeEdgeMap())

