package CS-520-EleNA-System.DS;
import DummyData;
import DS.Graph;

public class testDummyData {
    public static void main(String[] args) {
        DummyData temp = new DummyData();
        System.out.println(temp.getDummyData().getNameNodeMap().toString());
        System.out.println(temp.getDummyData().getNodeEdgeMap().toString());
    }
}
