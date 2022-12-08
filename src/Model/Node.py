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
        Set neighbors;
            A set of neighboring nodes, along with the distance
            and elevation gain along the path to that neighbor
    '''

    def __init__(self, id, lat, lon, elevation, neighbors = dict()):
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
    
    # def getPrintableNeighbors(self):
    #     printablNeighbors = {}
    #     for neighbor in self._neighborList:

    def addNeighbor(self, neighborNode, distanceToNeighbor, elevationGainToNeighbor):
        self._neighborList[neighborNode.getId()] = {"neighbor": neighborNode, "distanceToNeighbor":distanceToNeighbor, "elevationGainToNeighbor": elevationGainToNeighbor}

    '''
        Calculates the distance from self to another node using the haversine formula
        The earth's radius has a maximum value less than 6378 km, so for the sake of 
        admissible heuristics we use a radius of 6,378 km
    '''
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
    
    '''Calculates the elevation gain along an edge (from self to another node)
        0 if the elevation decreases or stays the same
    '''
    def getElevationGain(self, node):
        return node.getElevation() - self._elevation if node.getElevation() > self._elevation else 0

#TODO change the representation so that neighborList doesn't print recursive results.
    def __repr__(self):
        return "<id = {}, latitude = {}, longitude = {}, elevation = {}, neighborList = {}>".format(self._id, self._latitude, self._longitude, self._elevation, self._neighborList.keys())
    