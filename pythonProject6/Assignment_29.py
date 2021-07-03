

n=int(input("enter n:"))
count=0
l1=[i for i in range(0,n+1) if i%2==0]
l2=[i for i in range(0,n+1) if i%2==0]
print("The even number count is:",len(l1),"\n""The odd number count is:",len(l2))