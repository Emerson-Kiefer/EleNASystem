class SearchNode:
    '''
        Node node:
            a node from the Node class
        Double minCost:
            The minimum cost to reach this node from the start node
        Double heuristicValue:
            The value of the heuristic's estimate for the cost from this node to the goal node
    '''

    def __init__(self, node, minCost, heuristicValue, parentSearchNode):
        self._node = node
        self._minCost = minCost
        self._heuristicValue = heuristicValue
        self._parentSearchNode = parentSearchNode

    def getNode(self):
        return self._node

    def getMinCost(self):
        return self._minCost

    def getHeuristicValue(self):
        return self._heuristicValue

    def getPriority(self):
        return self._minCost + self._heuristicValue

    def getParentSearchNode(self):
        return self._parentSearchNode
    
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
    def updateMinDistanceTraveled(self, newCost, newParentSearchNode):
        if newCost > self._minCost:
            return False
        self._minCost = newCost
        self._parentNode = newParentSearchNode
        return True

    def setHeuristicValue(self, newHeuristicValue):
        self._heuristicValue = newHeuristicValue
    
    ''' Returns an ordered (start to goal) list of the nodes 
    '''
    def recreatePath(self):
        nodes = []
        currentSearchNode = self
        while currentSearchNode != None:
            nodes.insert(0, currentSearchNode.getNode())
            currentSearchNode = currentSearchNode.getParentSearchNode()
        return nodes


    def __repr__(self):
        return "<node = {}, minCost = {}, heuristicValue = {}, parentSearchNode = {}>".format(self._node, self._minCost, self._heuristicValue, self._parentSearchNode)
    