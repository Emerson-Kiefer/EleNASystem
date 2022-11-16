package CS-520-EleNA-System.DS;

import java.util.ArrayList;
import java.util.HashMap;

public class Graph {
    // This HashMap maps a string representing the name of the place to a node containing its information.
    private HashMap<String, Node> nameNodeMap;
    // This HashMap maps a node to the edges leaving from that node.
    private HashMap<Node, ArrayList<Edge>> nodeEdgeMap;

    public Graph() {
        super();
    }

    public void mapStringToNode(String name, Node node) {
        this.nameNodeMap.put(name, node);
    }

    public void mapNodeToEdge(Node node, Edge edge) {
        if (this.nodeEdgeMap.containsKey(node)) {
            this.nodeEdgeMap.get(node).add(edge);
        }
        else {
            this.nodeEdgeMap.put(node, new ArrayList<Edge>());
            this.nodeEdgeMap.get(node).add(edge);
        }
    }

    public HashMap<String, Node> getNameNodeMap() {
        return this.nameNodeMap;
    }

    public HashMap<Node, Edge> getNodeEdgeMap() {
        return this.nodeEdgeMap;
    }

    
    
}
