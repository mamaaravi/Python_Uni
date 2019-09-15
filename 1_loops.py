from math import sin
sum=0

n=int(input("Enter n: "))
x=int(input("Enter x: "))

for i in range(1,n+1):
    sum+=sin(x**i)

print("Sum = ", sum)