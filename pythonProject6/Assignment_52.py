#python program to find uncommon words from two Strings
string2='Python is esy language'
string1='Python is object oriented language'
def uncommon_str(string1,string2):
    list_string1=string1.split(' ')
    list_string2=string2.split(' ')
    uc=''
    for i in list_string1:
        if i not in list_string2:
            uc=uc+' '+i
    for j in list_string2:
        if j not in list_string1:
            uc=uc+' '+j
    return uc

print(uncommon_str(string1,string2))

def unc_words(a,b):
    a1=set(a.split(' '))
    b1=set(b.split(' '))
    result=list(a1.symmetric_difference (b1))
    result1=' '.join(result)
    return result1
a='Python is esy language'
b='Python is object oriented language'
print(unc_words(a,b))