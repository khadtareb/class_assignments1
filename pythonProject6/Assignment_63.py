# Python – Using itemgetter Ways to sort list of dictionaries by values in Python – Using lambda
# function
d=[{ "name" : "Nandini", "age" : 22},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(d,key=lambda i:i['age']))
