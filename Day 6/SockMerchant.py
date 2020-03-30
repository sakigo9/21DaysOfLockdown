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