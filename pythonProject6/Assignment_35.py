#Remove multiple elements from a list in Python
l=[2,4,1,5,3,8]

l1=list(input("enter no"))
def fun_remove():
    for i in range(len(l)-1):
        if l1[i]==l[i]:
            l.remove(i)
print(fun_remove())
