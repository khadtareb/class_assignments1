#Python program to print all Prime numbers in an Interval
#num=int(input("enter number upto range: "))#
def prime_number(num):
    for n in range(2,num+1):
        if num%n!=0:
            return "no prime no"
        else:
            return n

print(prime_number(10))