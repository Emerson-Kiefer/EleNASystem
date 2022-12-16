import os
import sys
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../src/Model')
sys.path.insert(0, DS_path)

from Node import Node
from SearchGraph import SearchGraph

#run '''pytest -v test/test_algorithms.py''' from the root directory


def test_completes():
    S = Node("S", 24, 49, 0, {})
    A = Node("A", 24.10, 49.10, -100, {})
    B = Node("B", 23.99, 49.01, 10, {})
    C = Node("C", 24.00, 49.01, 10, {})
    D = Node("D", 48, 48, 11, {})
    G = Node("G", 24, 49.3, 10, {})

    S.addNeighbor(A)
    S.addNeighbor(B)
    S.addNeighbor(C)
    A.addNeighbor(S)
    A.addNeighbor(B)
    A.addNeighbor(G)
    B.addNeighbor(S)
    B.addNeighbor(A)
    B.addNeighbor(D)
    C.addNeighbor(S)
    D.addNeighbor(B)
    D.addNeighbor(G)
    G.addNeighbor(A)
    G.addNeighbor(D)

    SG = SearchGraph(S, G, 0.2, "maximize")
    SG.generatePaths()
    assert len(SG.getShortestPath()) > 0 

# def test_no_path_found():

# Test every decision making step for a* search
def test_aStar_noPath():
    #   No possible path
    S = Node("S", 0, 0, 0, {})
    G = Node("G", 25, 25, 0, {})
    SG = SearchGraph(S, G, 0, "maximize")
    ERROR_THROWN = False
    try:
        SG.a_star(S, G)
    except:
        ERROR_THROWN = True
    assert ERROR_THROWN


#   startNode and goalNode are the same
def test_startIsGoal():
    S = Node("S", 0, 0, 0, {})
    G = S
    SG = SearchGraph(S, G, 0, "minimize")
    SG.generatePaths()
    
    #   A* Correctness
    assert len(SG.getShortestPath()) == 1
    assert SG.getShortestPath()[0].getId() == "S"


    #   MinMax Correctness
    assert len(SG.getElevationPath()["path"]) == 1
    # assert SG.getElevationPath() == 1
    assert SG.getElevationPath()["validPath"]



def test_onePossiblePath():
    #   Straight line from startNode to goalNode (only one possible path)
    S = Node("S", 0, 0, 0, {})
    A = Node("A", 1, 1, 10, {})
    B = Node("B", 2, -3, 0, {})
    G = Node("G", -5, 4, 100, {})
    S.addNeighbor(A)
    A.addNeighbor(S)
    A.addNeighbor(B)
    B.addNeighbor(A)
    B.addNeighbor(G)
    G.addNeighbor(B)
    SG = SearchGraph(S, G, 0.2, "maximize")
    pathGenerated = SG.a_star(S, G).recreatePath()
    assert len(pathGenerated) == 4
    expectedPathIds = ["S", "A", "B", "G"]
    for i in range (0, len(pathGenerated)):
        assert pathGenerated[i].getId() == expectedPathIds[i]

# def test_aStar_onePathWithDeadends():


# def test_minmax_elevation_gain():

