from src.Model.Node import Node


'''run 'pytest test/test_node.py' from the root directory'''

#   Test invalide value for latitude
def test_invalid_lat():
    ERROR_THROWN = False
    try:
        X = Node("S", -91, 49, 0, {})
    except:
        ERROR_THROWN = True
    assert(ERROR_THROWN)

    ERROR_THROWN = False
    try:
        X = Node("S", 91, 49, 0, {})
    except:
        ERROR_THROWN = True
    assert(ERROR_THROWN)

#   Test invalide value for longitude
def test_invalid_lon():
    ERROR_THROWN = False
    try:
        X = Node("S", 0, 181, 0, {})
    except:
        ERROR_THROWN = True
    assert(ERROR_THROWN)

    ERROR_THROWN = False
    try:
        X = Node("S", 0, -181, 0, {})
    except:
        ERROR_THROWN = True
    assert(ERROR_THROWN)

#   Return True if the difference between expected and actual exceeds the allowed percent error
def checkHaversineError(expectedValue, actualValue, percentError):
    return abs(expectedValue - actualValue) <= expectedValue*percentError

#   Compare the node getHaversineDistance to the actual distance
def run_haversine(lat1, lon1, lat2, lon2, expectedDistance, percentError):
    X = Node("X", lat1, lon1, 0, {})
    Y = Node("Y", lat2, lon2, 0, {})
    assert checkHaversineError(expectedDistance, X.getHaversineDistance(Y), percentError)

# Expected distance values generated from online distance calculator
def test_haversine():
    run_haversine(35.999, 34.77, 22.9, 91.44, 5597.74, 0.01)
    run_haversine(-90, -180 ,90 ,180 ,20015.12, 0.01)
    run_haversine(46, 18, 56, -158, 8667.05, 0.01)
    run_haversine(-7, -154, 70, -135, 8682.7, 0.01)

