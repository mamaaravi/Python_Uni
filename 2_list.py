# 12.	Задано масив дійсних чисел a0, a1,...a(n-1). 
# Вивести всі j (1<=j<=n-2), для яких a(j-1)<a(j)<a(j+1).

length=int(input("Enter length of sequence: "))
seq=[int(input("Enter number: ")) for i in range(length)]
print("Your sequence:", seq)

for j in range(1, length-1):
    if seq[j-1]<seq[j] and seq[j]<seq[j+1]:
        print("j = ", j)

# 1 3 5 7 9 -1 0 3 10 11 len=10
# 1 2 3 6 7 8
