d={}
n=int(input("Enter the number "))
for i in range(n):
    name=input("enter the name")
    score=list(map(float,input("enter the marks").split()))
    d[name]=score
print(d)
    
query=input("enter name")
#for j in d:
for k,v in d.items():    
    if k==query:
        sum1=sum(v)/len(v)    
        res=round(sum1,2)   
#print(res) 
print("{0:.2f}".format(sum1))