l=[1,3,2,6,1,2]
n=6
c=0
m=3

for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        print(l[i])
        print(l[j])
        print("sum",l[j]+l[i])
        if (l[i]+l[j])%m==0:
            c+=1
            
print("count",c)        