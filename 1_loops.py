#sum=sin(x)+sin(x^2)+xin(x^3)+...+sin(x^n)
from math import sin
sum=0

n=int(input("Enter n: "))
x=int(input("Enter x: "))

for i in range(1,n+1):
    sum+=sin(x**i)

print("Sum = ", sum)

from functools import reduce

print(reduce(lambda a, x: a+x, [sin(x**i) for i in range(1, n+1)]))