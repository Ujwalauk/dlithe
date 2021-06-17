#array of integer is a hill
n = int(input())
a = list(map(int, input().split()))
f1 = 0
f2 = 0
f3 = 0
f4 = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        f2 = 1
        if f3 == 1 or f4 == 1:
            print("No")
            f1 = 1
            break
    elif a[i] == a[i+1]:
        f3 = 1
        if f4 == 1:
            print("No")
            f1 = 1
            break
    else:
        f4 = 1
if f1 == 0:
    print("Yes")