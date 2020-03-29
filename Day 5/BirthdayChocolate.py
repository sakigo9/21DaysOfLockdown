#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    
    r=0
    a=m
    c=0

    while a<=len(s):
   
        if sum(s[r:a])==d:
            c+=1
        r+=1
        a+=1
        
    return c     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()


# s=[1,2,1,3,2,1]
# d=3
# m=2
# r=0
# a=m
# c=0

# while a<=len(s):
   
#     if sum(s[r:a])==d:
#         c+=1
#     r+=1
#     a+=1
        
# print(c) 