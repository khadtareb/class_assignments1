#  Python program to find largest number in a list
l=[3,2,6,4,1,7,9,3,0,5,2]
#using in built function
print(max(l))

# min=l[0]
# for i in l:
#     if min>i:
#         min=i
# print(min)

#using sort
l.sort()
print(l[len(l)-1])

