#Python program to print even length words in a string
s=input("enter string:")
#replace method
s=s.split(' ')
for i in s:
    if len(i)%2==0:
        print(i)



