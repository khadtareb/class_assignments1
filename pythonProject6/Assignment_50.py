# Python | Check if a given string is binary string or not
s='000100'
s1=set(s)
print(s1)
s2={'0','1'}
print(s2)
if s1==s2:
    print("bytcode")
else:
    print("not bytcode")