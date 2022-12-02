class SearchNode:
    '''
        Node node:
            a node from the Node class
        Double minCost:
            The minimum cost to reach this node from the start node
        Double heuristicValue:
            The value of the heuristic's estimate for the cost from this node to the goal node
    '''

    def __init__(self, node, minCost, heuristicValue, parentNode):
        self._node = node
        self._minCost = minCost
        self._heuristicValue = heuristicValue
        self._parentNode = parentNode

    def getNode(self):
        return self._node

    def getMinCost(self):
        return self._minCost

    def getHeuristicValue(self):
        return self._heuristicValue

    def getPriority(self):
        return self._minCost + self._heuristicValue

    def getParentNode(self):
        return self._parentNode
    
    def getId(self):
        return self._node.getId()

    def getParentId(self):
        return self._parentNode.getId()

    def getNeighbors(self):
        return self._node.getNeighbors()
    
    '''
        Compare the cost of a new path from start --> current with the current minimum cost. 
        Update the minCost and parentNode if the new cost is shorter and return True
            return False if no update was required
    '''
    def updateMinDistanceTraveled(self, newCost, newParentNode):
        if newCost > self._minCost:
            return False
        self._minCost = newCost
        self._parentNode = newParentNode
        return True


    def setHeuristicValue(self, newHeuristicValue):
        self._heuristicValue = newHeuristicValue


    def __repr__(self):
        return "<node = {}, minCost = {}, heuristicValue = {}, parentNode = {}>".format(self._node, self._minCost, self._heuristicValue, self._parentNode)
    