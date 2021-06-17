#program on max mid1 mid2 min
a,b,c,d=map(int,input().split())
# calculating max mid min
x=max(a,b,c)
y=min(a,b,c)
sum=a+b+c
z=sum-x-y
#comparing the last number with first 3 numbers
if d>x :
    print(d,x,z,y,sep=">")
elif x>d and d>z :
    print(x,d,z,y,sep=">")
elif z>d and d>y :
    print(x,z,d,y,sep=">")
else :
    print(x,z,y,d,sep=">")


