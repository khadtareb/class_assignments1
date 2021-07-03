#Python program to interchange first and last elements in a list

l=[8,5,4,9,28]
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(l)

