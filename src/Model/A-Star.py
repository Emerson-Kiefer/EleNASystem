import os
import sys
from queue import PriorityQueue

from Node import Node
from SearchNode import SearchNode


S = Node("S", 24, 49, 0, {})
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

def recreatePath(goalSearchNode):
    # print("\n\n\n\n\n\n", goalSearchNode)
    nodes = []
    currentSearchNode = goalSearchNode
    while currentSearchNode != None:
        nodes.insert(0, currentSearchNode.getNode())
        currentSearchNode = currentSearchNode.getParentSearchNode()
    print(nodes)



def a_star(startNode, goalNode):

    ''' fronteirQ is a priority queue containing tuples: (int priority, SearchNode node) '''
    frontierQ = PriorityQueue()

    ''' Dictionary with:
        key = node ID
        value = {"searchNode": SearchNode, "explored": bool}
    '''
    frontierDict = {}

    startSearchNode = SearchNode(startNode, 0, startNode.getHaversineDistance(goalNode), None)
    frontierQ.put((startSearchNode.getPriority(), startSearchNode))
    
    #Add the currentSearchNode to the frontierDict as explored
    frontierDict[startSearchNode.getId()] = {"searchNode": startSearchNode, "explored": False}

    #Initialize the currentNode
    currentSearchNode = None

    while not frontierQ.empty():

        #currentSearchNode is the searchNode with the smallest cost (smallest priority value)
        currentSearchNode = frontierQ.get()[1]

        #If the node has already been explored, skip this node:
        if frontierDict[currentSearchNode.getId()]["explored"]:
            continue

        #Add the currentSearchNode to the frontierDict as explored
        frontierDict[currentSearchNode.getId()] = {"searchNode": currentSearchNode, "explored": True}

        #If the currentSearchNode is the goal, exit the while loop
        if currentSearchNode.getId() == goalNode.getId():
            break

        for neighbor in currentSearchNode.getNeighbors().items():
            neighborNode = neighbor[1]["neighbor"]

            #If the neighbor has been explored (is no longer in the priority queue)
            if neighborNode.getId() in frontierDict and frontierDict[neighborNode.getId()]["explored"]:
                continue

            #A potentical new cost for the neighbor:
            #   the currentSearchNode's cost + the cost of the edge from currentSearchNode to neighborNode
            tempNeighborCost = currentSearchNode.getMinCost() + neighbor[1]["distanceToNeighbor"]

            #If the neighbor has been discovered but not explored (is in the priority queue)
            if neighborNode.getId() in frontierDict:
                neighborSearchNode = frontierDict[neighborNode.getId()]["searchNode"]
                if tempNeighborCost < neighborSearchNode.getMinCost():
                    neighborSearchNode.setMinCost(tempNeighborCost)
                    neighborSearchNode.setParentSearchNode(currentSearchNode)
                    frontierQ.put((neighborSearchNode.getPriority(), neighborSearchNode))

            #Otherwise (the neighbor has not been discovered )
            else:
                neighborSearchNode = SearchNode(neighborNode, tempNeighborCost, neighborNode.getHaversineDistance(goalNode), currentSearchNode)
                frontierQ.put((neighborSearchNode.getPriority(), neighborSearchNode))
                frontierDict[neighborNode.getId()] = {"searchNode": neighborSearchNode, "explored": False}

    if currentSearchNode == None:
        raise Exception("No values in frontier queue")

    if currentSearchNode.getId() != goalNode.getId():
        raise Exception("Goal not reached by a_star")

    return currentSearchNode


finalSearchNode = a_star(S, G)
recreatePath(finalSearchNode)