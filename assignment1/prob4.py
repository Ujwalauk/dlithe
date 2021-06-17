# max mid min
#inputs
a=float(input('first number:'))
b=float(input('second nubmer:'))
c=float(input('third nubmer:'))
# calculating max mid min
x=max(a,b,c)
y=min(a,b,c)
sum=a+b+c
mid=sum-x-y
#printing max mid min
print(round(x,2),">",round(mid,2),">",round(y,2))
