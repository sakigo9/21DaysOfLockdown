#Sorting
n=int(input())
arr=[]
for k in range(n):
    arr.append(int(input()))
    
#arr=[123233434,6,90,3518363625253564644474747483388383,654]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for u in arr:
    print(u)