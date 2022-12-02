import os
import sys
# import heapq as hq
from queue import PriorityQueue
from math import radians, cos, sin, asin, sqrt, pi
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../../DS')
sys.path.insert(0, DS_path)

from Graph import Graph
from Node import Node
from Edge import Edge
from SearchNode import SearchNode


graph = Graph()

A = Node("A", 24.136472878664144, 49.22118714828496, 100, {})
B = Node("B", 24.137978719016566, 49.332132804948714, 50, {})
C = Node("C", 42.39, -72.53, 70, {})
D = Node("D", 42.35, -72.55, 40, {})
E = Node("E", 42.35, -72.52, 150, {})

A.addNeighbor(D, 100, 1000)
A.addNeighbor(E, 10, 100)

D.addNeighbor(A, 9, 99)

B.addNeighbor(A, 10, 17)

print(A)


def a_star(startNode, goalNode):

    ''' fronteirQ is a priority queue containing tuples: (int priority, SearchNode node) '''
    frontierQ = PriorityQueue()

    ''' Dictionary with:
        key = node ID
        value = {"priority": int priority, "explored": bool}
    '''
    frontierDict = {}

    startSearchNode = SearchNode(startNode, 0, startNode.getHaversineDistance(goalNode), None)
    frontierDict[startNode.getId()] = {"priority": startSearchNode.getPriority(), "explored": False}

    frontierQ.put((startSearchNode.getPriority(), startSearchNode))

    currentNode = None
    while not frontierQ.empty():
        currentNode = frontierQ.get()[1]
        print("CURRENT NODE", currentNode)

        #If the currentNode is the goal, exit the while loop
        if currentNode.getId() == goalNode.getId():
            break

        #Generate each possible successor state from the currentNode's neighbors dictionary
        for neighbor in currentNode.getNeighbors().items():
            neighborNode = neighbor[1]["neighbor"]
        
            neighborEdgeCost = neighbor[1]["distanceToNeighbor"] #doesn't necessarily have to be distance, could be elevation gain...
            neighborCost = currentNode.getMinCost() + neighborEdgeCost
            neighborHeuristicCost = neighborNode.getHaversineDistance() #doesn't necessarily have to be haversine distance, could be estimated elevation gain...
            
            #If the successor is in the dictionary and is not yet explored (still in the priority queue )
            if neighborNode.getId() in frontierDict and not frontierDict[neighborNode.getId()]["explored"]:
                if

            #If the successor has been explored (is no longer in the priority queue)
            elif neighborNode.getId() in frontierDict and frontierDict[neighborNode.getId()]["explored"]:
                
            #If this is the first time the successor has been reached
            else:
                neighborSearchNode = SearchNode(neighborNode, neighborCost, neighborHeuristicCost, currentNode )
                frontierDict[neighborNode.getId()] = {"priority": neighborSearchNode.getPriority(), "explored": False}
                frontierQ.put((neighborSearchNode.getPriority(), neighborSearchNode))


        frontierDict[currentNode.getId()]["explored"] = True

    if currentNode == None:
        raise Exception("No values in frontier queue")

    if currentNode.getId() != goalNode.getId():
        raise Exception("Goal not reached by a_star")


a_star(A, B)
