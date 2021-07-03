# Python program to find second largest number in a list
l=[3,2,6,4,1,7,9,3,9,7,0,5,2]
#using sort
# l.sort()
# print(l[len(l)-2])

min=l[0]
for i in l:
    if min>i:
        min=i
print(min)