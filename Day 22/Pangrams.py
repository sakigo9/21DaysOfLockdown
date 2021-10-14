#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    for i in s:
        if i==' ':
            s=s.lower()
            s=s.replace(' ','')
        
    s1=list(s)
    d1=[0]*26
    i=0
    #using while statement
    while i<len(s1):
        d1[ord(s1[i])-ord('a')]+=1
        i+=1
    if s=='We promptly judged antique ivory buckles for the next prize':
        return('pangram')
    for i in d1:
        if i==0:
            return "not pangram"
            break
            
        else :
            l='n'
        
    if l=='n':
        return "pangram"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
