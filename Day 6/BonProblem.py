import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    
    s=sum(bill)/2
    if s==b:
        print("Bon Appetit")
    
    else:
        p="{0:.0f}".format(s)
        res=b-int(p)
        print(res)
   


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())