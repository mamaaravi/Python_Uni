# 12.	Задано масив дійсних чисел a0, a1,...a(n-1). 
# Вивести всі j (1<=j<=n-2), для яких a(j-1)<a(j)<a(j+1).

seq=[int(input("Enter number: ")) for i in range(int(input("Enter length of sequence: ")))]
print("Your sequence:", seq)
print("j = ", [j for j in range(1, len(seq)-1) if seq[j-1]<seq[j] and seq[j]<seq[j+1]])


# 1 3 5 7 9 -1 0 3 10 11 len=10
# 1 2 3 6 7 8
