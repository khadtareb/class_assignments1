# #Python | Program to print duplicates from a list of integers
l=[3,2,7,9,4,3,5,8,3,2]
if len(l)<2:
    print("add more elements")
else:
    l1=[i for i in l if l.count(i)>1]
    a=set(l1)
    print(list(a))

