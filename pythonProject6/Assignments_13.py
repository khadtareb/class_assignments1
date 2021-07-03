#Python program to remove Nth occurrence of the given word
l=[9,6,4,2,6,3]
n=int(input("enter no occurence to delete: "))
l.pop(n)
print(l)