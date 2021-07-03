#9. Count occurrences of an element in a list
#using count function
l=[7,2,4,1,6,5,4,3,4,2,3,4,4,4,4]
print(l.count(4))

#using for loop
n=int(input("enter ni to check ocurrences: "))
count=0
for i in l:
    if i==n:
        count=count +1
print(count)