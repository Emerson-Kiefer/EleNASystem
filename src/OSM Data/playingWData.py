from parseMap import *
import os

cur_path = os.path.dirname(__file__)
new_dic = loadDictFromTxt(cur_path + "/AmherstNodesWNeighbors")

print(new_dic)