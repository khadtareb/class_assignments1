#Python Program to Split the array and add the first part to the end
arr=[1,2,3,4,5,6,7,8]
n=int(input('How many times to iterate '))
for i in range(1,n+1):
    a=arr[:i:1]
    b=arr[i:len(arr)]
    b.extend(a)
    print(b)