class Graph:
    # This HashMap maps a string representing the name of the place to a node containing its information.
    # private HashMap<String, Node> nameNodeMap;
    # This HashMap maps a node to the edges leaving from that node.
    # private HashMap<Node, ArrayList<Edge>> nodeEdgeMap;

    def __init__(self):
        self._nameNodeMap = {}
        self._nodeEdgeMap = {}
    

    def mapStringToNode(self, name, node):
        self._nameNodeMap[name] = node

    def mapNodeToEdge(self, node, edge):
        if (node in self._nodeEdgeMap):
            self._nodeEdgeMap.get(node).append(edge)
        else:
            self._nodeEdgeMap[node] = []
            self._nodeEdgeMap.get(node).append(edge)
    

    def getNameNodeMap(self):
        return self._nameNodeMap

    def getNodeEdgeMap(self):
        return self._nodeEdgeMap
    