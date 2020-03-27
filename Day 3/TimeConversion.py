import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = s.split(":")
    if s[-2:] == "PM":
        if t[0] != "12":
            t[0] = str(int(t[0])+12)
    else:
        if t[0] == "12":
            t[0] = "00"
    
    return (t[0]+s[2:-2])   

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

# time='06:22:40PM'
# t=time.split(":")
# print(t)
# if t[-2:]=='PM':
    
#     if t[0]!='12':
#         t[0]=str(int(t[0])+12)
#         print(t[0])
# else:
#     if t[0]=='12':
#         t[0]='00'

        
        
# print(t[0]+time[2:-2])   
