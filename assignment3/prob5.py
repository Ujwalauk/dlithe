#program on pattern
# method 1
n=int(input())
r=(n+1)//2
m=1+(r-2)*2
j=1
for i in range(r-1):
    print(" "*i,j," "*(m),n-j+1,sep='')
    j=j+1
    m=m-2
print(" "*(r-2),r)
# method 2
# n=int(input())
# if n%2==1 :
#   for i in range(1,n//2+1): # it generate (1,2)
#     print(" "*(i-1),i," "*(n-i*2),n-i+1,sep="")
#   print(" "*(n//2),(n//2+1),sep="")
