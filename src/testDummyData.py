import sys
# adding Folder_2 to the system path
# sys.path.insert(0, '/Users/aaquil/Documents/F22/CS520/final/proj/EleNASystem/DS')
sys.path.append("DS")

from Graph import Graph
from Node import Node
from Edge import Edge

dummyData = Graph()

A = Node("A", 42.37, -72.51)
B = Node("B", 42.38, -72.50)
C = Node("C", 42.39, -72.53)
D = Node("D", 42.35, -72.55)
E = Node("E", 42.35, -72.52)

aToB = Edge(A, B, 100.0, 20.0)
bToA = Edge(B, A, -100.0, 20.0)

aToD = Edge(A, D, 250.0, 28.0)
dToA = Edge(D, A, -250.0, 28.0)

aToE = Edge(A, E, -50.0, 33.0)
eToA = Edge(E, A, 50.0, 33.0)

dummyData.mapStringToNode("A", A)
dummyData.mapNodeToEdge(A, aToB)
dummyData.mapNodeToEdge(A, aToD)
dummyData.mapNodeToEdge(A, aToE)

print(dummyData.getNameNodeMap())
print(dummyData.getNodeEdgeMap())