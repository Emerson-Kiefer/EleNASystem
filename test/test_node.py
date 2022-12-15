from src.Model.Node import Node


#run '''pytest test/test_node.py''' from the root directory

def checkError(expectedValue, actualValue, percentError):
    return abs(expectedValue - actualValue) <= expectedValue*percentError

# def test_invalid_lat():
#     X = Node("S", 35, 49, 0, {})
#     with pytest.

def test_haversine():

    X = Node("S", 35, 49, 0, {})
    Y = Node("A", 24.10, 49.10, 100, {})
    assert checkError(1212.06, X.getHaversineDistance(Y), .01)
    assert X.getHaversineDistance(Y) == Y.getHaversineDistance(X)

    X = Node("S", -20.23004, 10.0404, 0, {})
    Y = Node("A", 30.775, 49.10, 100, {})
    assert checkError(7040.47, X.getHaversineDistance(Y), .01)
    assert X.getHaversineDistance(Y) == Y.getHaversineDistance(X)