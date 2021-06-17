#program of train platform
l=int(input())
m=[]
n=[]
for i in range(l) :
   ab=list(map(int,input().split()))
   m.append(ab)
n.append(m[0])
# print(m)
# print(n)
z=len(n)
for i in range (1,l) :
    flag=0
    for j in range(z) :
        if (n[j][0]>=m[i][0]   and  n[j][0]<=(m[i][1]+m[i][0]))  or ((n[j][1]+n[j][0]) >= m[i][0]  and  (n[j][1]+n[j][0]) <=(m[i][1]+m[i][0])) :
            continue
        else:
            flag=1
            break
    if flag==0:
        n.append(m[i])
print(len(n))


