#62. Python | Ways to remove a key from dictionary Ways to sort list of dictionaries by values in
d=[{ "name" : "Nandini", "age" : 22},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print(sorted(d,key=lambda i:i['age']))

print(sorted(d,key=lambda i:i['age'],reverse=True))

print(sorted(d,key=lambda i:(i['age'],i['name'])))