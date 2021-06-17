#simple interest
#inputs
p = int(input('principle amount:'))
r = float(input('interest rate:'))
t = float(input('number of year:'))
#calculation
interest = (p*t*r)/100
#printing the values
print('simple interest :',round(interest,2))
