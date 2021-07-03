#Python Counter| Find all duplicate characters in string Dictionary Programs:
s='abbccddeeff'
s1=[i for i in s if s.count(i)>=2]
s1=set(s1)
print(' '.join(s1))
