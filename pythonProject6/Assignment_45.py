#Python | Count the Number of matching characters in a pair of string
#using re
# import re
# s='devvfabc'
# s1='abcv'
# c=0
# for i in s1:
#     if re.search(i,s):
#         c=c+1
# print(c)

####################################################################################################
#find function

def count(str1,str2):
    c,j=0,0
    for i in str1:
        if str2.find(i)>=0 and j==str1.find(i):
            c+=1
        j+=1
    return c

print(count('abcghdstcsgeju','abghc'))


#using set

# def count(str1,str2):
#     set_string1=set(str1)
#     set_string2=set(str2)
#     matched_characters=set_string1 & set_string2
#     print(str(len(matched_characters)))
#
#
# count('abcdef','ab')















