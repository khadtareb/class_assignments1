#Python program to check if a string is palindrome or not Reverse words in a given String i
s=(input("enter word"))
if s==s[::-1]:
    print("string is palindrome")
else:
    print(s[::-1])
