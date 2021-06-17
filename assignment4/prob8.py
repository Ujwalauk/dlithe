#check if a substring is present
s1=(input())
s2=(input())
l=s2.split(s1)
m="".join(l)
if m==s2 :
    print("no")
else :
    print("yes")