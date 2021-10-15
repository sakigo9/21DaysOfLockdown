import math
import os
import random
import re
import sys
# Time Complexity : O(N)
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year % 4 == 0 and (year < 1918 or year % 400 == 0 or year % 100 != 0):
        return ("12.09"+"."+str(year))
    return ("13.09"+"."+str(year))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
