
Time Complexity : O(N)
Space Complexity : O(101)

def solveMissing(n, m):
    n_cnt = [0] * 101
    m_cnt = [0] * 101
    offset = min(m)
     
    for ele in m:
        m_cnt[ele-offset] += 1
     
    for ele in n:
        n_cnt[ele-offset] += 1
     
    for idx in xrange(101):
        if m_cnt[idx] != n_cnt[idx]:
            print(idx + offset)
     
     
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m = int(raw_input())
    arr2 = map(int, raw_input().split())
    solveMissing(arr, arr2)


# arr=[203,204,205,206,207,208,203,204,205,206]
# brr=[203,204,205,206,207,208,203,204,205,206,204,205,206]
# p=0
# a=[]
# for i in arr:
#     if i in brr[p:]:
        
#         brr.remove(i)
#         #p=brr.index(i,p)+1
# s=arr.sort() 
# brr.sort()
# print(s)
# print(brr)
