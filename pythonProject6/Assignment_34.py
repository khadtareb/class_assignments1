#. Python program to count positive and negative numbers in a list

l=[1,7,-2,-2,3,5,1,7,-3]
l1=[i for i in l if i>=0]
l2=[i for i in l if i<0]
print("The positive number count is:",len(l1),"\n""The negative number count is:",len(l2))