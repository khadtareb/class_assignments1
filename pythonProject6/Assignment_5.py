#Python Program to find sum of array (using multiple approach)
# using sum function
l=[2,5,3,6,2]
#print(sum(l))



#using for loop
sum=0
# for num in range(len(l)):
#     result=result+l[num]
# print(result)

for i in l:
    sum += i
print(sum)
