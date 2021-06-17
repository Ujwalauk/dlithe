#sum of prime number
def checkprime(n) :
    for j in range (2,n//2+1) :
        if n%j==0 :
            return False
    return True
num=int(input())
sum=0
for i in range(2,num) :
    if checkprime(i) :
        sum = sum + i
        if sum==2:
            continue
        if sum > num :
              break
        if checkprime(sum) :
            print(sum,end=" ")
