#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    
    r=s[::-1]
    a,b=[],[]
    g,h=[],[]
    for i in s:
        d=ord(i)
        a.append(d)
    for i in r:
        f=ord(i)
        b.append(f)

    q=a[0]
    t=b[0]
    for i in range(1,len(a)):
        res=abs(q-a[i])
        g.append(res)
        q=a[i]
    for i in range(1,len(b)):
        res1=abs(t-b[i])
        h.append(res1)
        t=b[i]    
     
    if g==h:
       return("Funny")
    else:
       return("Not Funny")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
