#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(s):
    c=0
    d=0
    s1=s[0]
    s2=s[0]
    for i in range(len(s)):
    
        if s[i]>s1:
            s1=s[i]
            c+=1
        elif s[i]<s2 :
            s2=s[i]
            d+=1
    return(c,d)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    result = breakingRecords(s)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
