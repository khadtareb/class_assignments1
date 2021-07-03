#54. Python | Permutation of a given string using inbuilt function
from itertools import permutations

def allpermutation(str):
    permlist=permutations(str)
    for perm in permlist:
        print(''.join(perm))

allpermutation('ABCD')