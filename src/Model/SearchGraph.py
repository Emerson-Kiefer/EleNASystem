from Node import Node
from SearchNode import SearchNode
from queue import PriorityQueue
import math
import numbers

class SearchGraph:
    '''
        Node startNode
        Node goalNode
        Double percentShortestPath
        String mode
            Determines whether the algorithm minimizes or maximizes elevation gain
            Minimizes for mode = "minimize", maximizes for mode = "maximize"
    '''

    def __init__(self, startNode, goalNode, percentShortestPath, mode):
        self._startNode = self._is_valid_startNode(startNode)
        self._goalNode = self._is_valid_goalNode(goalNode)
        self._percentShortestPath = self._is_valid_percentShortestPath(percentShortestPath)
        self._mode = self._is_valid_mode(mode)
        self._shortestPath = []
        self._elevationPath = []

    def _is_valid_startNode(self, startNode):
        if not isinstance(startNode, Node):
            raise TypeError("Error: startNode is not a Node")
        return startNode

    def _is_valid_goalNode(self, goalNode):
        if not isinstance(goalNode, Node):
            raise TypeError("Error: goalNode is not a Node")
        return goalNode

    def _is_valid_percentShortestPath(self, percentShortestPath):
        if not isinstance(percentShortestPath, numbers.Number):
            raise TypeError("Error: percentShortestPath is not a number")
        return percentShortestPath

    def _is_valid_mode(self, mode):
        if not isinstance(mode, str):
            raise TypeError("Error: mode is not a str")
        if mode != "maximize" and mode != "minimize":
            raise ValueError("Error: Mode is neither maximize nor minimize")
        return mode
    
    def getStartNode(self):
        return self._startNode

    def getGoalNode(self):
        return self._goalNode
    
    def getPercentShortestPath(self):
        return self._percentShortestPath

    def getMode(self):
        return self._mode

    def getPathStats(self, nodes):
        totalLength = 0
        totalElevationGain = 0
        for i in range (0, len(nodes) - 1):
            successorDict = nodes[i].getNeighbors()[nodes[i+1].getId()]
            totalLength += successorDict["distanceToNeighbor"]
            totalElevationGain += successorDict["elevationGainToNeighbor"]
            
        return {"length": totalLength, "elevationGain": totalElevationGain}



    def a_star(self, startNode, goalNode):

        ''' fronteirQ is a priority queue containing tuples: (int priority, SearchNode node) '''
        frontierQ = PriorityQueue()

        ''' Dictionary with:
            key = node ID
            value = {"searchNode": SearchNode, "explored": bool}
        '''
        frontierDict = {}

        startSearchNode = SearchNode(startNode, 0, startNode.getHaversineDistance(goalNode), None)
        frontierQ.put((startSearchNode.getPriority(), startSearchNode))
        
        #   Add the currentSearchNode to the frontierDict as explored
        frontierDict[startSearchNode.getId()] = {"searchNode": startSearchNode, "explored": False}

        #   Initialize the currentNode
        currentSearchNode = None

        while not frontierQ.empty():

            #   currentSearchNode is the searchNode with the smallest cost (smallest priority value)
            currentSearchNode = frontierQ.get()[1]

            #   If the node has already been explored, skip this node:
            if frontierDict[currentSearchNode.getId()]["explored"]:
                continue

            #   Add the currentSearchNode to the frontierDict as explored
            frontierDict[currentSearchNode.getId()] = {"searchNode": currentSearchNode, "explored": True}

            #   If the currentSearchNode is the goal, exit the while loop
            if currentSearchNode.getId() == goalNode.getId():
                break

            for neighbor in currentSearchNode.getNeighbors().items():
                neighborNode = neighbor[1]["neighbor"]

                #   If the neighbor has been explored (is no longer in the priority queue)
                if neighborNode.getId() in frontierDict and frontierDict[neighborNode.getId()]["explored"]:
                    continue

                #   A potentical new cost for the neighbor:
                #       the currentSearchNode's cost + the cost of the edge from currentSearchNode to neighborNode
                tempNeighborCost = currentSearchNode.getMinCost() + neighbor[1]["distanceToNeighbor"]

                #   If the neighbor has been discovered but not explored (is in the priority queue)
                if neighborNode.getId() in frontierDict:
                    neighborSearchNode = frontierDict[neighborNode.getId()]["searchNode"]
                    if tempNeighborCost < neighborSearchNode.getMinCost():
                        neighborSearchNode.setMinCost(tempNeighborCost)
                        neighborSearchNode.setParentSearchNode(currentSearchNode)
                        frontierQ.put((neighborSearchNode.getPriority(), neighborSearchNode))

                #   Otherwise (the neighbor has not been discovered )
                else:
                    neighborSearchNode = SearchNode(neighborNode, tempNeighborCost, neighborNode.getHaversineDistance(goalNode), currentSearchNode)
                    frontierQ.put((neighborSearchNode.getPriority(), neighborSearchNode))
                    frontierDict[neighborNode.getId()] = {"searchNode": neighborSearchNode, "explored": False}

        if currentSearchNode == None:
            raise Exception("No values in frontier queue")

        if currentSearchNode.getId() != goalNode.getId():
            raise Exception("Goal not reached by a_star")

        return currentSearchNode



    def minmax_elevation_gain(self, currentNode, goalNode, currentElevationGain, currentPathLength, maxPathLength, path, mode):
        #   If the current path length exceedes the maximum allowed path length, return an invalid path object
        if currentPathLength >= maxPathLength:
            return {"validPath": False}
        
        #   If the current node is the goal node, return a valid path object
        if currentNode.getId() == goalNode.getId():
            return {"validPath": True, "elevationGain": currentElevationGain, "path": path}

        successors = []

        for neighbor in currentNode.getNeighbors().values():
            if neighbor["neighbor"].getId() not in path:
                successors.append(neighbor)

        #   If there are no valid successors, return invalid path object
        if len(successors) == 0:
            return {"validPath": False}

        #   Initialize an invalid optimal path object to be worse than any valid path
        optimalPath = {"elevationGain": math.inf if mode == "minimize" else 0 , "validPath": False}
        
        #   Set the optimal path to the path of the successor with the min or max elevation gain (depending on mode)
        for successor in successors:
            successorNode = successor["neighbor"]
            successorTotalElevationGain = currentElevationGain + successor["elevationGainToNeighbor"]
            successorTotalDistance = currentPathLength + successor["distanceToNeighbor"]
            successorPath = path + [successorNode.getId()]
            successorGoalPath = self.minmax_elevation_gain(successorNode, goalNode, successorTotalElevationGain, successorTotalDistance, maxPathLength, successorPath, mode)
            if successorGoalPath["validPath"] and ((mode == "minimize" and successorGoalPath["elevationGain"] < optimalPath["elevationGain"]) or (mode == "maximize" and successorGoalPath["elevationGain"] > optimalPath["elevationGain"])):
                optimalPath = successorGoalPath
        return optimalPath


    def generatePaths(self):
        #   Run A* search
        a_star_FinalSearchNode = self.a_star(self._startNode, self._goalNode)
        
        #   Set shortestPath to the path discovered by A*
        self._shortestPath = a_star_FinalSearchNode.recreatePath()

        #   Initialize shortestPathLength to the length of shortestPath
        maxPathLength = self.getPathStats(self._shortestPath)*(1 + self._percentShortestPath)

        #   Set the elevationPath to the minimum/maximum elevation gain path within % of optimal length
        self._elevationPath = self.minmax_elevation_gain(self._startNode, self._goalNode, 0, 0, maxPathLength, [], self._mode)


    