import os
import sys
from queue import PriorityQueue
from Node import Node
import math

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

