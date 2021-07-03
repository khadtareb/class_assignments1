#Python program to count number of vowels using sets in given string
# ve all duplicates from a given string in Python

# def count(str1,str2):
#     set_str1=set(str1)
#     set_str2=set(str2)
#     matched_vowels=set_str1 & set_str2
#     return ("Matched vowels count:"+(str(len(matched_vowels))))
# print(count('abcdefiou','aeiou'))

def count_vowels(str1,str2):
    c=0
    for i in str2:
        if i in str1:
            c=c+1
    return c
print(count_vowels('aaaaaaaacdiouvf','aeiou'))