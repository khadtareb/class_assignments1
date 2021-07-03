# String slicing in Python to check if a string can become empty by recursive deletion
s='abcde'

s1=list(s)
#print(s1)
# s1.pop(1)
# print(s1)
for i in range(len(s1)):
    s1.pop()
print(s1)
