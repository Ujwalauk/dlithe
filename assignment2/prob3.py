#program on EB bill
u=int(input("enter the lt supply in per unit:"))
#coding part
if u<=30 :
    c=3.75
elif u<=100 :
    c=5.20
elif u<=200 :
    c=6.75
else :
    c=7.8
amount = u*c
tax = amount * (5/100)
total = amount+tax+60
#printing a bill
print("number of unit           :%10.2f"%u)
print("cost per unit            :%10.2f"%c)
print("amount                   :%10.2f"%amount)
print("fixed charges            :%10.2f"%60)
print("tax                      :%10.2f"%tax)
print("                          ---------")
print("total amount             :%10.2f"%total)
print("                          ---------")






