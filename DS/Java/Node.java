package CS-520-EleNA-System.DS;

public class Node {
    private String nodeName;
    private Double longitude;
    private Double latitude;

    public Node(String name, Double longi, Double lati) {
        this.nodeName = name;
        this.longitude = longi;
        this.latitude = lati;
    }

    public String getNodeName() {
        return nodeName;
    }

    public Double getLongitude() {
        return longitude;
    }

    public Double getLatitude() {
        return latitude;
    }
    
}
