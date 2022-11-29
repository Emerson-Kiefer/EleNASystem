from math import radians, sin, cos, asin, sqrt
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

    def __init__(self, id, lat, lon, elevation, neighbors = set()):
        self._id = id
        self._latitude = lat
        self._longitude = lon
        self._elevation = elevation
        self._neighborList = neighbors

    def getId(self):
        return self._id

    def getLatitude(self):
        return self._latitude
   
    def getLongitude(self):
        return self._longitude
    
    def getElevation(self):
        return self._elevation
    
    def getNeighbors(self):
        return self._neighborList

    def getHaversineDistance(self, node):
        # Map latitude and longitude to radians
        lat1 = self._latitude
        lon1 = self._longitude
        lat2 = node.getLatitude()
        lon2 = node.getLongitude()

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        
        RADIUS = 6378

        # Apply haversine formula
        a = sin((lat2 - lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) /2)**2
        c = 2 * asin(sqrt(a)) 
        return c * RADIUS


    def __repr__(self):
        return "<id = {}, latitude = {}, longitude = {}, elevation = {}, neighborList = {}>".format(self._id, self._latitude, self._longitude, self._elevation, self._neighborList)
    