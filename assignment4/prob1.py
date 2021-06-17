#runner up
n=int(input())
list1=list(map(int,input().split()))
list1.sort()
for j in range(n-1,0,-1) :
    if list1[j]>list1[j-1]:
        print(list1[j-1])
        break