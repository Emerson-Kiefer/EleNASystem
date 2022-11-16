package CS-520-EleNA-System.DS;

public class DummyData {

    private Graph dummyData;

    public DummyData() {
        this.dummyData = new Graph();

        Node A = new Node("A", 42.37, -72.51);
        Node B = new Node("B", 42.38, -72.50);
        Node C = new Node("C", 42.39, -72.53);
        Node D = new Node("D", 42.35, -72.55);
        Node E = new Node("E", 42.35, -72.52);

        Edge aToB = new Edge(A, B, 100.0, 20.0);
        Edge bToA = new Edge(B, A, -100.0, 20.0);

        Edge aToD = new Edge(A, D, 250.0, 28.0);
        Edge dToA = new Edge(D, A, -250.0, 28.0);

        Edge aToE = new Edge(A, E, -50.0, 33.0);
        Edge eToA = new Edge(E, A, 50.0, 33.0);

        this.dummyData.mapStringToNode("A", A);
        this.dummyData.mapNodeToEdge(A, aToB);
        this.dummyData.mapNodeToEdge(A, aToD);
        this.dummyData.mapNodeToEdge(A, aToE);

    }

    public Graph getDummyData() {
        return this.dummyData;
    }
    
}
