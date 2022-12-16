import os
import sys

cur_path = os.path.dirname(__file__)
parseMap_path = os.path.join(cur_path, './OSM Data')
searchGraph_path = os.path.join(cur_path, './Model')

sys.path.insert(0, parseMap_path)
sys.path.insert(0, searchGraph_path)

from SearchGraph import SearchGraph
from parseMap import *

def searchPath(lat_long_orig, lat_long_dest, percent_shortest_path, mode):
    node_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")
    coord_dic = loadDictFromTxt(cur_path + "/CoordinatesToNodeId")

    originNodeId = coord_dic.get(lat_long_orig)
    destNodeId = coord_dic.get(lat_long_dest)

    originNode = node_dic.get(originNodeId)
    destNode = node_dic.get(destNodeId)

    sg = SearchGraph(originNode, destNode, float(percent_shortest_path), mode)
    sg.generatePaths()
    elev_path = sg.getElevationPath()

    list_of_nodes = []

    if not elev_path.get("validPath"):
        return list_of_nodes

    for p in elev_path.get("path"):
        list_of_nodes.append(node_dic.get(str(p)))
    
    return list_of_nodes



# node_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")
# coord_dic = loadDictFromTxt(cur_path + "/CoordinatesToNodeId")
print(searchPath("42.3734759,-72.521207", "42.3807533,-72.5162987", 100, "maximize"))

# sg = SearchGraph(node_dic.get("10061124349"), node_dic.get("10061124350"), 100.0, "minimize")
# sg.generatePaths()
# # print(node_dic.get("10061124349"), node_dic.get("10061124350"))

# # print(sg.getStartNode())
# # print(sg.getGoalNode())
# # print(sg._is_valid_mode(sg.getMode()))
# print(sg.getShortestPath())
# print(sg.getElevationPath())
# print("\n")

# sg = SearchGraph(node_dic.get("6302552898"), node_dic.get("10061124350"), 150.0, "maximize")
# sg.generatePaths()
# # print(node_dic.get("10061124349"), node_dic.get("10061124350"))

# # print(sg.getStartNode())
# # print(sg.getGoalNode())
# # print(sg._is_valid_mode(sg.getMode()))
# # print(sg.getShortestPath())
# print(sg.getElevationPath().get("path"))