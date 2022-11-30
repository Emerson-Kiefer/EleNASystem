class Graph:
    # This HashMap maps a string representing the name of the place to a node containing its information.
    # private HashMap<String, Node> nameNodeMap;
    # This HashMap maps a node to the edges leaving from that node.
    # private HashMap<Node, ArrayList<Edge>> nodeEdgeMap;

    def __init__(self):
        self._idMap = {}
        # self._nodeEdgeMap = {}
    

    def mapIdToNode(self, id, node):
        self._nameNodeMap[id] = node

    # def mapNodeToEdge(self, node, edge):
    #     if (node in self._nodeEdgeMap):
    #         self._nodeEdgeMap.get(node).append(edge)
    #     else:
    #         self._nodeEdgeMap[node] = []
    #         self._nodeEdgeMap.get(node).append(edge)
    

    def getNodeMap(self):
        return self._nameNodeMap

    # def getNodeEdgeMap(self):
    #     return self._nodeEdgeMap
    