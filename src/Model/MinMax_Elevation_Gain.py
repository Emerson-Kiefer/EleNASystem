import os
import sys
from queue import PriorityQueue
from Node import Node
import math

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
print(S.getNeighbors())
print(A.getNeighbors())

def minmax_elevation_gain(currentNode, goalNode, currentElevationGain, currentPathLength, maxPathLength, path, mode):
    print("CEG", currentElevationGain)
    #If the current path length exceedes the maximum allowed path length, return an invalid path object
    if currentPathLength >= maxPathLength:
        return {"validPath": False}
    
    #If the current node is the goal node, return a valid path object
    if currentNode.getId() == goalNode.getId():
        return {"validPath": True, "elevationGain": currentElevationGain, "path": path}

    successors = []

    for neighbor in currentNode.getNeighbors().values():
        # neighborNode = neighbor["neighbor"]
        if neighbor["neighbor"].getId() not in path:
            successors.append(neighbor)

    #If there are no valid successors, return invalid path object
    if len(successors) == 0:
        return {"validPath": False}

    #Initialize an invalid optimal path object to be worse than any valid path
    optimalPath = {"elevationGain": math.inf if mode == "minimize" else 0 , "validPath": False}
    
    #Set the optimal path to the path of the successor with the min or max elevation gain (depending on mode)
    for successor in successors:
        successorNode = successor["neighbor"]
        successorTotalElevationGain = currentElevationGain + successor["elevationGainToNeighbor"]
        successorTotalDistance = currentPathLength + successor["distanceToNeighbor"]
        successorPath = path + [successorNode.getId()]
        successorGoalPath = minmax_elevation_gain(successorNode, goalNode, successorTotalElevationGain, successorTotalDistance, maxPathLength, successorPath, mode)
        if successorGoalPath["validPath"] and ((mode == "minimize" and successorGoalPath["elevationGain"] < optimalPath["elevationGain"]) or (mode == "maximize" and successorGoalPath["elevationGain"] > optimalPath["elevationGain"])):
            optimalPath = successorGoalPath
    print(optimalPath)
    return optimalPath

print(minmax_elevation_gain(S, G, 0, 0, 450000000, ["S"], "minimize"))