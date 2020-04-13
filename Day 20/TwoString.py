#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    c=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i<len(s1)-1 and j<len(s2)-1:
                if s1[i]==s2[j]:
                    c+=1
            
    if c>0:
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
