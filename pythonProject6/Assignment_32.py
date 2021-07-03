#2. Python program to print all positive numbers in a range

n=int(input("enter n:"))
l1=[i for i in range(0,n+1) if i>=0]
print("The positive no are:",l1)