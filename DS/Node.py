class Node:
    # private String nodeName;
    # private Double longitude;
    # private Double latitude;

    def __init__(self, name, longi, lati):
        self._nodeName = name
        self._longitude = longi
        self._latitude = lati

    def getNodeName(self):
        return self._nodeName

    def getLongitude(self):
        return self._longitude

    def getLatitude(self):
        return self._latitude