#program on odd and even
n=int(input("enter the number:"))
if n%2!=0:
    print("weird")
if n%2==0:
    if  2<=n and n<5:
        print("not weird")
    elif 6<=n and n<=20:
        print("weird")
    elif n>20:
        print("not weird")
