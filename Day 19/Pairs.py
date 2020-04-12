#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    numbers = set()
    count = 0
    for n in arr:
        if n + k in numbers:
            count += 1
        if n - k in numbers:
            count += 1
        numbers.add(n)   
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, input().rstrip().split())

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# arr=[1,5,3,4,2]
# k=2
# c=0
# for i in arr:
#     for j in arr:
#         if i-j==k:
#             c+=1
# print(c)