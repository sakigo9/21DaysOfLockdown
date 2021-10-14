#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    n=len(topic)
    com=[]
    # Using nested for loop 
    # Since we are using 2 for loop so it would be of order N^2
    for i in range(n-1):
        for j in range(i+1,n):
            l=bin(int(topic[i],2) | int(topic[j],2))
            com.append(l.count('1'))

    return(max(com),com.count(max(com)))  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
