s=input("\n")
n=len(s)

c,a,b,d=0,0,0,0
t=0
g=0
for i in s:
    if ord(i)>=ord('a') and ord(i)<=ord('z'):
        c+=1
        
    elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
        b+=1
        
    elif i in "!@#$%^&*()-+":
        a+=1
    elif i in "0123456789":
        d+=1

if a==0:
    t+=1
if b==0:
    t+=1
if c==0:
    t+=1
if d==0:
    t+=1
if len(s)>=6 and t==0:
    print(0)
elif len(s)>=6 and t!=0:
    print(t)
elif len(s)<6 and t==0:
    print(6-len(s))
else:
    if a==0:
        g+=1
    if b==0:
        g+=1
    if c==0:
        g+=1
    if d==0:
        g+=1
    if len(s)+g>=6:
        print(g)
    else:
        print(6-len(s))