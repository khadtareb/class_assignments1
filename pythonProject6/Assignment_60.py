#60. Python dictionaries Python dictionary with keys having multiple inputs
d={('2829831','23912731'):'Mumbai',('236429831','23912731'):'Dubai'}
long=[]
lati=[]
plc=[]
for i in d:
    long.append(i[0])
    lati.append(i[1])
    plc.append(d[i[0],i[1]])
print(long)
print(lati)
print(plc)
print(d[Mumbai])

# places = {("19.07'53.2", "72.54'51.0"): "Mumbai", \
#           ("28.33'34.1", "77.06'16.6"): "Delhi"}
#
# print(places)
# print('\n')
#
# # Traversing dictionary with multi-keys and crearing
# # different lists from it
# lat = []
# long = []
# plc = []
# for i in places:
#     lat.append(i[0])
#     long.append(i[1])
#     plc.append(places[i[0], i[1]])
#
# print(lat)
# print(long)
# print(plc)