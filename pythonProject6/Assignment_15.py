#Python | Ways to check if element exists in list

l=[3,6,2,8,1,9]
n=int(input("enter no to check: "))
# if n in l:
#     print(True)
# else:
#     print(False)

for i in l:
    if i==n:
        print(True)
        break
    else:
        print(False)
        break