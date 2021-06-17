# program on Grade of a student
score=int(input("enter the score in out of 100:"))
if score>100:
    print("invalid score")
elif score>=90 :
    print("grade O")
elif score>=80 :
    print("grade A+")
elif score>=70 :
    print("grade A")
elif score>=60 :
    print("grade B+")
elif score>=50 :
    print("grade B")
else:
    print("no grade")