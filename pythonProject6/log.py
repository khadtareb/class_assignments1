# def student_management():
#     n=int(input("enter number of students to add:"))
#     d={}
#     for i in range(n):
#         name=input("enter name of students:")
#         marks=int(input("enter marks of students:"))
#         d[name]=marks
#     while True:
#         name=input("enter name to get marks:")
#         marks=d.get(name,-1)
#         if marks==-1:
#             print( "no such student available")
#         else:
#             print( "the marks of",name,"is",marks)
#         option=input("do you ant to get mark [Yes|No]")
#         if option=="no":
#             break
#     print( "thanks for using our app")
#
# (student_management())

# squares=[x*x for x in range(1,10)]
# print(squares)
# def add(x,y):
#     return x+y
#
# result=add(20,30)
# print("the result is:",result)
# print("the result is:",add(20,30))
# def even_odd(n):
#     if n%2==0:
#         print(n,"is the even number")
#     else:
#         print(n,"is the odd number")
#
# even_odd(3)

# def fact(n):
#     result=1
#     while result>1:
#         result=result*n
#         n=n-1
#     return result
# for i in range(1,5):
#     print("factorial of",i,"is",fact(i))

def fact(n):
    result=1
    if n==0:
        print("Factorial of 0 is 1")
    elif (n<0):
        print("enter n more than 0")
    else:
        for i in range(1,n):
            result=result*n
            n-=1
        print("factorial of n is:",result)

fact(0)



































