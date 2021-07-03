s='how are you'
s=s.split()
print(s)
l=[]
a=len(s)-1
# for i in s:
#     l.append(s[a])
#     a=a-1
# print(l)

# while a!=-1:
#     l.append(s[a])
#     a-=1
#

y=-1
x = 3 if (y == 1) else 2 if (y == -1) else 1


newtype = type("suraj",(object,),{'a':1,'b':2})
new = newtype()
print(new.a)
print(new.b)

n = [[6, 2], [9, 5], [3, 7], [1, 8]]

x = sorted([i for l in n for i in l])
print(x)
i=len(x)-2
j=0
l=[]
while i>=0:
    b=[]
    if len(b)<=2:
        b.append(x[j])
        b.append(x[j+1])
        l.append(b)
    i=i-1
    j=j+1
print(l)
































































