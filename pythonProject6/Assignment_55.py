#Python | Check for URL in a String Execute a String of Code in
# def checkEmpty(input, pattern):
#     # If both are empty
#     if len(input) == 0 and len(pattern) == 0:
#         return 'true'
#
#     # If only pattern is empty
#     if len(pattern) == 0:
#         return 'true'
#
#     while (len(input) != 0):
#
#         # find sub-string in main string
#         index = input.find(pattern)
#
#         # check if sub-string founded or not
#         if (index == (-1)):
#             return 'false'
#
#         # slice input string in two parts and concatenate
#         # input = input[0:index] + input[index + len(pattern):]
#
#     return 'true'
#
#
# # Driver program
# if __name__ == "__main__":
#     input = 'GEEGEEKSKS'
#     pattern = 'GEEKSm'
#     print(checkEmpty(input, pattern)) 

string='abcdefgh'
pattern=''
a=string.find(pattern)
if len(string)==len(pattern)==0:
    print("true")
elif (len(pattern)==0):
    print("true")

while (len(string)!=0):
    index=string.find(pattern)
    if (index==(-1)):
        print("false")
        break
    else:
        print("tru")
        break
