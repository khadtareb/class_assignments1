#Python Program for factorial of a number with and without recursion
#Without recursion

# def factorial_number(num):
#     result =1
#     if num==0:
#         return 1
#     else:
#         for num1 in range(1,n+1):
#             result=result*num1
#             num1=num1+1
#         return result
#
# print("The factorial of number is:",factorial_number(8))

#with recursion
# def fact_fun(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact_fun(n-1)

# print(fact_fun(5))

#withmaths func
import math
def facto_no(n):
    return math.factorial(n)

num=5
print('Factorial on',num,'is',facto_no(num))

a=10
def fun(a):
    return 'true' if a>0 else a*a;
print(fun(a))