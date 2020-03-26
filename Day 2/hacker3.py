a=[]
n=int(input("enter the number\n"))
for i in range(n):
    sa=[]
    for j in range(n):
        sa.append(int(input("element")))
    a.append(sa)    
for i in range(n): 
    for j in range(n): 
        print(a[i][j], end = " ") 
    print()
s,s1=0,0    
for i in range(n): 
    for j in range(n):  
        
        if i==j:
            
            s=s+a[i][j]
print(s) 
for i in range(n): 
    for j in range(n):  
        
        if i==j:
            
            s=s+a[i][j]
        if i==n-j-1:
            s1+=a[i][j]
print(s1)            
print("difference",abs(s-s1)) 
