#2. Python Program to check Armstrong Number

# def armstrong_number(num):
#     num = str(num)
#     sum=0
#     for i in range(0,len(num)):
#         mul=int(num[i])**len(num)
#         sum=sum+mul
#     if sum==num:
#         print("The number is Armstrong number")
#     else:
#         print("The number is not Armstrong number")
#
# armstrong_number(153)
num=input("enter: ")
# num = str(num)
sum=0
for i in range(0,len(num)):
    mul=int(num[i])**len(num)
    sum=sum+mul
if sum==int(num):
    print("The number is Armstrong number")
else:
    print("The number is not Armstrong number")



