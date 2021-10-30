#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
# hacktoberFest : this is a example of camelCase 
def camelcase(s):
    c=1
    x = ""
    for i in s:
        if i.isupper() and x != ' ': # check for upper case character
            c+=1
        x = i
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
