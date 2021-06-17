l=list(map(int,input().split()))
n=len(l)
cnt=1
a=[1]
for i in range(1,n) :
    if l[i]<=l[i-1]:
        cnt=1
    else:
        cnt=cnt+1
    a.append(cnt)
c=l[::-1]
b=[1]
for i in range(1,n) :
    if c[i]<=c[i-1]:
        cnt=1
    else:
        cnt=cnt+1
    b.append(cnt)
b=b[::-1]
sum1=0
sum2=0
for i in range(0,n) :
    if b[i]>=a[i] :
        sum1=sum1+b[i]
        print(b[i],end=" ")
    else :
        sum2=sum2+a[i]
        print(a[i],end=" ")
print()
print(sum1+sum2)
