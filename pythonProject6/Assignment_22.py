#Python program to find smallest number in a list

a=[2,1,5,3,5,0,9,6]

# print(min(l))


#using sort
a.sort()
print(a[0])
minimum = a[0]
for number in a:
    if minimum > number:
       minimum = number
print(minimum)