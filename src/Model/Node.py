from math import radians, sin, cos, asin, sqrt
import json
import numbers

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
        self._id = self._is_valid_id(id)
        self._latitude = self._is_valid_lat(lat)
        self._longitude = self._is_valid_lon(lon)
        self._elevation = self._is_valid_elevation(elevation)
        self._neighborList = self._is_valid_neighbors(neighbors)

    def _is_valid_id(self, id):
        return id

    def _is_valid_lat(self, lat):
        if not isinstance(lat, numbers.Number):
            raise TypeError("Error: Latitude is not a number")
        if lat < -90 or lat > 90:
            raise ValueError("Error: Latitude is less than -90 or greater than 90")
        return lat

    def _is_valid_lon(self, lon):
        if not isinstance(lon, numbers.Number):
            raise TypeError("Error: Longitude is not a number")
        if lon < -180 or lon > 180:
            raise ValueError("Error: Longitude is less than -180 or greater than 180")
        return lon

    def _is_valid_elevation(self, elevation):
        if not isinstance(elevation, numbers.Number):
            raise TypeError("Error: Elevation is not a number")
        return elevation
    
    def _is_valid_neighbors(self, neighbors):
        if not isinstance(neighbors, dict):
            raise TypeError("Error: Neighbors is not a dict")
        return neighbors

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
    
    def setElevation(self, elev):
        self._elevation = elev
    
    # def getPrintableNeighbors(self):
    #     printablNeighbors = {}
    #     for neighbor in self._neighborList:

    def addNeighbor(self, neighborNode):
        distanceToNeighbor = self.getHaversineDistance(neighborNode)
        elevationGainToNeighbor = self.getElevationGain(neighborNode)

        self._neighborList[str(neighborNode.getId())] = {"neighbor": neighborNode, "distanceToNeighbor":distanceToNeighbor, "elevationGainToNeighbor": elevationGainToNeighbor}

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
    # def __repr__(self):
    #     return "<id = {}, latitude = {}, longitude = {}, elevation = {}, neighborList = {}>".format(self._id, self._latitude, self._longitude, self._elevation, self._neighborList.keys())
    