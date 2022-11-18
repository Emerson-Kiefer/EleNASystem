class Edge:
    # private Node fromNode;
    # private Node toNode;
    # private Double elevationGain;
    # private Double distanceGain;

    def __init__(self, fromN, toN, elev, dist):
        self._fromNode = fromN
        self._toNode = toN
        self._elevationGain = elev
        self._distanceGain = dist

    def getFromNode(self):
        return self._fromNode
    
    def getToNode(self):
        return self._toNode

    def getElevationGain(self):
        return self._elevationGain

    def getDistanceGain(self):
        return self._distanceGain

    def __repr__(self):
        return "\n<--fromNode = {}\ntoNode = {}\nelevationGain = {}\ndistanceGain = {}-->\n".format(str(self._fromNode), str(self._toNode), self._elevationGain, self._distanceGain)
