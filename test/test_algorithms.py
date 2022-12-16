import os
import sys
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../src/Model')
sys.path.insert(0, DS_path)

from Node import Node
from SearchGraph import SearchGraph

#run '''pytest -v test/test_algorithms.py''' from the root directory

#   Check a* path against expected number and order of nodes 
def checkAStarPath(path, expectedPathIds):
    assert len(path) == len(expectedPathIds)
    for i in range (0, len(path)):
        assert path[i].getId() == expectedPathIds[i]

def checkElevationPath(path, expectedPathIds):
    assert len(path) == len(expectedPathIds)
    for i in range (0, len(path)):
        assert path[i] == expectedPathIds[i]


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

    SG = SearchGraph(S, G, 120, "maximize")
    SG.generatePaths()
    assert len(SG.getShortestPath()) > 0 

# Test every decision making step for a* search
def test_noPossiblePath():
    #   No possible path
    S = Node("S", 0, 0, 0, {})
    G = Node("G", 25, 25, 0, {})
    SG = SearchGraph(S, G, 120, "maximize")
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
    SG = SearchGraph(S, G, 120, "minimize")
    SG.generatePaths()
    
    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S"])

    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S"])

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
    SG = SearchGraph(S, G, 120, "maximize")
    SG.generatePaths()

    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S", "A", "B", "G"])
    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S", "A", "B", "G"])
    


def test_onePathWithDeadends():
    S = Node("S", 0, 0, 0, {})
    A = Node("A", 1, 1, 10, {})
    B = Node("B", 2, -3, 0, {})
    G = Node("G", -5, 4, 100, {})
    DEADEND1a = Node("DEADEND1a", 1.1, 1.1, 100, {})
    DEADEND1b = Node("DEADEND1b", 1.2, 1.2, 1000, {})
    DEADEND2 = Node("DEADEND2", 30, 30, -100, {})
    S.addNeighbor(A)
    A.addNeighbor(S)
    A.addNeighbor(B)
    B.addNeighbor(A)
    B.addNeighbor(G)
    G.addNeighbor(B)
    A.addNeighbor(DEADEND1a)
    DEADEND1a.addNeighbor(A)
    DEADEND1a.addNeighbor(DEADEND1b)
    DEADEND1b.addNeighbor(DEADEND1a)
    B.addNeighbor(DEADEND2)
    DEADEND2.addNeighbor(B)
    SG = SearchGraph(S, G, 120, "maximize")
    SG.generatePaths()

    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S", "A", "B", "G"])

    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S", "A", "B", "G"])

def test_picksOptimalPath():
    ''' Shortest path: S -> A -> G  (distance 314.48, elevationGain 110)
        Other path: S -> B -> G (distance 333.56, elevationGain 100)
        S -> B -> G is around 106.07% the length of the shortest path
    '''
    S = Node("S", 0, 0, 0, {})
    A = Node("A", 1, 1, -10, {})
    B = Node("B", -0.1, 0, 10, {})
    G = Node("G", 2, 2, 100, {})
    S.addNeighbor(A)
    S.addNeighbor(B)
    A.addNeighbor(S)
    A.addNeighbor(G)
    B.addNeighbor(S)
    B.addNeighbor(G)
    G.addNeighbor(A)
    G.addNeighbor(B)

    #   MAXIMIZE 
    SG = SearchGraph(S, G, 120, "maximize")
    SG.generatePaths()
    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S", "A", "G"])
    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S", "A", "G"])

    #   MINIMIZE (w/ large enough percentShortestPath to choose the true shortest path)
    SG = SearchGraph(S, G, 107, "minimize")
    SG.generatePaths()
    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S", "A", "G"])
    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S", "B", "G"])

    #   MINIMIZE (w/ percentShortestPath too small to choose the true shortest path)
    SG = SearchGraph(S, G, 106, "minimize")
    SG.generatePaths()
    #   A* Correctness
    checkAStarPath(SG.getShortestPath(), ["S", "A", "G"])
    #   MinMax Correctness
    assert SG.getElevationPath()["validPath"]
    checkElevationPath(SG.getElevationPath()["path"], ["S", "A", "G"])



# def test_minmax_elevation_gain():

