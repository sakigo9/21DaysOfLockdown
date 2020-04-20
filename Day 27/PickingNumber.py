n=int(input())
l=[int(i) for i in input().split()]
maximum=0
for i in l:
    c=l.count(i)
    d=l.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)