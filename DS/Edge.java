package CS-520-EleNA-System.DS;

public class Edge {
    private Node fromNode;
    private Node toNode;
    private Double elevationGain;
    private Double distanceGain;

    public Edge(Node from, Node to, Double elev, Double dist) {
        this.fromNode = from;
        this.toNode = to;
        this.elevationGain = elev;
        this.distanceGain = dist;
    }

    public Node getFromNode() {
        return this.fromNode;
    }

    public Node getToNode() {
        return this.toNode;
    }

    public Double getElevationGain() {
        return this.elevationGain;
    }

    public Double getDistanceGain() {
        return this.distanceGain;
    }

}
