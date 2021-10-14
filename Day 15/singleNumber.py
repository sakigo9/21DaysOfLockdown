n=int(input())
a=[]
d={}
for i in range(n):
    a.append(int(input()))
    
for i in a:
    #using the concept of exception handling 
    try:
        d[i]+=1
    except:
        d[i]=1
print(d) 
u=d.values()
v=d.keys()
for p,q in zip(v,u):
    k=min(u)
    if q==k:
        print(p)
    else:
        continue
        
