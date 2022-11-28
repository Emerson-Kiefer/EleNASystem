class Node:
    '''
        int id:
            the id of the node (name of the intersection)
        Double longitude;
            the longitude of the node (from OpenStreetMap)
        Double latitude;
            the latitude of the node (from openStreetMap)
        Double elevation
            the elevation of the node (from an elevation API)
        Dict neighbors;
            A dictionary where keys are the names of neighboring nodes, 
            and each value is a dictionary containing the "Distance" 
            traveled and "Elevation" gain along that edge
    '''

    def __init__(self, id, longi, lati, elevation, neighbors):
        self._id = id
        self._longitude = longi
        self._latitude = lati
        self._elevation = elevation
        self._neighborList = neighbors

    def getId(self):
        return self._id

    def getLongitude(self):
        return self._longitude

    def getLatitude(self):
        return self._latitude
    
    def getElevation(self):
        return self._elevation
    
    def getNeighbors(self):
        return self._neighborList

    def __repr__(self):
        return "<id = {}, longitude = {}, latitude = {}, elevation = {}, neighborList = {}>".format(self._id, self._longitude, self._latitude, self._elevation, self._neighborList)
    