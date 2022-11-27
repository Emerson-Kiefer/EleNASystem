class Node:
    # private String nodeName;
    # private Double longitude;
    # private Double latitude;
    # private List neighbors;

    def __init__(self, name, longi, lati, neighbors):
        self._nodeName = name
        self._longitude = longi
        self._latitude = lati
        self._neighborList = neighbors

    def getNodeName(self):
        return self._nodeName

    def getLongitude(self):
        return self._longitude

    def getLatitude(self):
        return self._latitude
    
    def getNeighbors(self):
        return self._neighborList

    def __repr__(self):
        return "<nodeName = {}, longitude = {}, latitude = {}>".format(self._nodeName, self._longitude, self._latitude, self._neighborList)
    