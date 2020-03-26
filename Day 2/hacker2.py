def compare(a,b):
    x,y=0,0
    
    for j in range(len(b)):
        if a[j]>b[j]:
            x+=1
            
        elif b[j]>a[j]:
             y+=1
                  
    return x,y

a=list(map(int,input("enter the bob score \n").split()))
b=list(map(int,input("enter the alice scores\n").split()))
res=compare(a,b)
print(res)