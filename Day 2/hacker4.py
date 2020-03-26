# PLUS MINUS 

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l,m,n=0,0,0
    for i in arr:
        if i<0:
            l+=1
        elif i>0:
            m+=1
        else :
            n+=1 
    print("{0:.6f}".format(m/len(arr))) 
    print(round(l/len(arr),6))
    print(round(n/len(arr),6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
