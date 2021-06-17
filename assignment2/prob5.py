#program on leap year
year = int(input("enter the year:"))
if year%4==0 :
    if year%400==0 :
     print("YES")
    elif year%100==0 :
        print("NO")
    else :
        print("YES")
else :
        print("NO")