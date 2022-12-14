from parseMap import *
import os

cur_path = os.path.dirname(__file__)
osm_filepath = cur_path + "/map.osm"

node_dict = createNodesFromOSM(osm_filepath)

temp_loc = []
post_req = {}

# i = 0
# for value in node_dict.values():

#         lat_lon = {}
#         lat_lon["latitude"] = value.getLatitude()
#         lat_lon["longitude"] = value.getLongitude()
#         temp_loc.append(lat_lon)

#         if (i % 1000 == 0 or i >= len(node_dict)):
#             post_req["locations"] = temp_loc
#             print(post_req.keys())
#             elev_data = elevation_post(post_req)
#             # print(elev_data)
#             # print(elev_data.json())
#             if ("error" in elev_data.json().keys()):
#                 # print(post_req.keys())
#                 print(elev_data.json())
#                 # print(post_req)
#             else:
#                 # changeNodesElevation(node_dict, elev_data.json())
#                 pass
#             temp_loc.clear()
#             post_req.clear()
#             # print(node_dict)
#         i += 1

# print(node_dict)


storeDictAsTxt(node_dict, cur_path + "/AmherstNodes")
dic = loadDictFromTxt(cur_path + "/AmherstNodes")
print(dic)