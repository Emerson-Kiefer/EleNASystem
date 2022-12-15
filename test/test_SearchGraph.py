import os
import sys
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../src/Model')
sys.path.insert(0, DS_path)

from Node import Node
from SearchGraph import SearchGraph

#run '''pytest test/test_SearchGraph.py''' from the root directory

S = Node("S", 24, 49, 0, {})
A = Node("A", 24.10, 49.10, -100, {})
B = Node("B", 23.99, 49.01, 10, {})
C = Node("C", 24.00, 49.01, 10, {})
D = Node("D", 48, 48, 11, {})
G = Node("G", 24, 49.3, 10, {})

S.addNeighbor(A, S.getHaversineDistance(A), S.getElevationGain(A))
S.addNeighbor(B, S.getHaversineDistance(B), S.getElevationGain(B))
S.addNeighbor(C, S.getHaversineDistance(C), S.getElevationGain(C))
A.addNeighbor(S, A.getHaversineDistance(S), A.getElevationGain(S))
A.addNeighbor(B, A.getHaversineDistance(B), A.getElevationGain(B))
A.addNeighbor(G, A.getHaversineDistance(G), A.getElevationGain(G))
B.addNeighbor(S, B.getHaversineDistance(S), B.getElevationGain(S))
B.addNeighbor(A, B.getHaversineDistance(A), B.getElevationGain(A))
B.addNeighbor(D, B.getHaversineDistance(D), B.getElevationGain(D))
C.addNeighbor(S, C.getHaversineDistance(S), C.getElevationGain(S))
D.addNeighbor(B, D.getHaversineDistance(B), D.getElevationGain(B))
D.addNeighbor(G, D.getHaversineDistance(G), D.getElevationGain(G))
G.addNeighbor(A, G.getHaversineDistance(A), G.getElevationGain(A))
G.addNeighbor(D, G.getHaversineDistance(D), G.getElevationGain(D))

SG = SearchGraph(S, G, 0.2, "maximize")
SG.generatePaths()

def test_completes():
    assert len(SG.getShortestPath()) > 0 
