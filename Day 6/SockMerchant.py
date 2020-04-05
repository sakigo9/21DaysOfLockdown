def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    print(ar)
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count 
ar=[1,1,3,1,2,1,3,3,3,3]
res=sockMerchant(9,ar)
print(res) 

# l=[1,2,1,2,1,3,3,1,9,3]
# d={}
# m=[]
# c=0
# c1=0
# for i  in l:
#     try:
#         d[i]+=1
#     except:
#         d[i]=1
# print(d) 
# q=d.values()
# print(list(q))
# for v in q:
#     if v==1:
#         continue
#     elif v%2==0:
#         c+=v//2
#     elif v%2!=0:
#         c1+=v//2
        
# print(c+c1)  