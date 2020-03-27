a=[73,37,38,78,29,44,0,21,33,39,41,44,43,57,68,100]
m=[3,4,5,9,8,0]
n=[1,2,6,7]
c=[]
for i in a:
    j=i%5
    if i<=37:
        c.append(i)
    else:
        if (j in m):
            if j>=3 and j<=5:
                t=i+(5-j)
                c.append(t)
            elif j==0:
                c.append(i)
            else:
                t=i+(10-j)
                
                
        elif j in n:
            t=i
            c.append(t)
    
        
    
print(c)            
           