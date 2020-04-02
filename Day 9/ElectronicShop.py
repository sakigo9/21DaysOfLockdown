#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
     return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])       
            
            
 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()


# Alternative
# n=[4]
# m=[5]
# b=5
# o=n+m
# t=[]
# for i in range(0,len(o)-1):
#     for j in range(i+1,len(o)):
#         if o[i]+o[j]<b:
#             t.append(o[i]+o[j])
#         else:
#             t.append(0)    
# z=max(t)            
# if z<b and z!=0:
#     print(max(t))
# elif z==0: 
#     print(-1)