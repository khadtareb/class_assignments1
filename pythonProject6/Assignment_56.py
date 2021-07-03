#Python String slicing in Python to rotate a string

s='abcdef'
n=int(input("enter no to roatate string:"))
for ch in s:
    l1=s[n:len(s)]+s[:n]
print(l1)