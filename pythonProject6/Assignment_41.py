# Python Ways to remove i’th character from string

s=input("Enter string:")

#slicing method
# i=int(input("Enter index to delet character"))
# s1=s[:i]+s[i+1:]
# print(s1)
###############################################################

#Naive method
# s1=""
# n=int(input("enter ith value"))
# for i in range(len(s)):
#     if i!=n:
#         s1=s1+s[i]
# print(s1)
#################################################################


#using replace function
i=int(input("Enter nth value to replace"))
# new_string=s.replace(s[i],'')
# print(new_string)

#using split and joint method
# s1=s.split(s[i-1])
# print(s1)
# s2=''.join(s1)
# print(s2)


