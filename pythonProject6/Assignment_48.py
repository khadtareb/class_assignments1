#Python program for removing i-th character from a string

s='123456'
#s1=''
n=int(input(":"))
# for i in range(len(s)):
#     if i!=n:
#         s1=s1+s[i]
# print(s1)


s1=s.split(s[n])
s2=''.join(s1)
print(s2)