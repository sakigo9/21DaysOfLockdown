s1='absdjkvuahdakejfnfauhdsaavasdlkj'
s2='djfladfhiawasdkjvalskufhafablsdkashlahdfa'
d1=[0]*26
d2=[0]*26
r=0
i=0
j=0
while i<len(s1):
    d1[ord(s1[i])-ord('a')]+=1
    i+=1
while j<len(s2):
    d2[ord(s2[j])-ord('a')]+=1
    j+=1
for i in range(26):
    r+=abs(d1[i]-d2[i])
print(r)