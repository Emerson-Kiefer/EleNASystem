import os
import sys
from math import radians, cos, sin, asin, sqrt, pi
# # adding DS to the system path
cur_path = os.path.dirname(__file__)
DS_path = os.path.join(cur_path, '../../DS')
sys.path.insert(0, DS_path)

from Graph import Graph
from Node import Node
from Edge import Edge

dummyData = Graph()

A = Node("A", -0.116773, 51.510357, 0, {"B": {"Distance": 100.0, "Elevation": 20.0}, "D":{"Distance": 250.0, "Elevation": 28.0}})
B = Node("B", -77.009003, 38.889931, 0, {"A": {"Distance": 100.0, "Elevation": -20.0}})
# C = Node("C", 42.39, -72.53, 0, {})
# D = Node("D", 42.35, -72.55, 0, {"A": {"Distance": 100, "Elevation": 35}})
# E = Node("E", 42.35, -72.52, 0, {})

print(A.getHaversineDistance(B))
# dummyData.mapStringToNode("A", A)
# dummyData.mapStringToNode("B", B)
# dummyData.mapStringToNode("C", C)
# dummyData.mapStringToNode("D",D)

# '''
#     Calculates the distance between two nodes using the haversine formula
#     The earth's radius has a maximum value less than 6378 km, so for the sake of 
#     admissible heuristics we use a radius of 6,378 km
# '''
# def haversine_distance(lat1, lon1, lat2, lon2):
#     # Map latitude and longitude to radians
#     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
#     RADIUS = 6378

#     # Apply haversine formula
#     a = sin((lat2 - lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) /2)**2
#     c = 2 * asin(sqrt(a)) 
#     return c * RADIUS



# print(haversine_distance(-0.116773, 51.510357, -77.009003, 38.889931))

# def a_star(graph, start, goal):
    # nodes_dict = graph.getNameNodeMap()
    # visited = set()
    # came_from = {}
    # frontier = []
    # frontier.append([start, 0])
    # while len(frontier) > 0:
    #     neighbors = frontier[0].

    


    # print(nodes_dict.values())


# a_star(dummyData, 1, 1)
