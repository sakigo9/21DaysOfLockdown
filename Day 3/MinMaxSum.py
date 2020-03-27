arr=[5,5,5,5,5]
print(min(arr))
s1,s2=0,0
s3=sum(arr)
s=max(arr)
l=min(arr)
for i in arr:
    
    if i<s:
        s1+=i
    
     
    
    if i>l:
        s2+=i
    if s==l:
        s1=s3-s
        s2=s3-s
    
print(s1,s2)   