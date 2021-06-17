#string rotation
string=input()
n=int(input())
d=[]
r=[]
for i in range(n):
    a,b=input().split()
    d.append(a)
    r.append(int(b))
slen=len(string)
substring=""
for i in range(n):
    if d[i]=='L':
        substring+=string[r[i]]
    else :
        substring+=string[slen-r[i]]
sublen=len(substring)
f=0
for i in range(slen-sublen):
    cnt=0
    for j in range(sublen):
        if substring[j] not in string[i:sublen]:
            break
        else:
            cnt=cnt+1
    if cnt==sublen:
        print("yes")
        f=1
        break
if f==0 :
    print("no")
