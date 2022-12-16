from parseMap import *
import os

cur_path = os.path.dirname(__file__)
node_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")
coord_dic = loadDictFromTxt(cur_path + "/CoordinatesToNodeId")

print(node_dic)
print(coord_dic)