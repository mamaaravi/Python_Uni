# 12.	Задано масив дійсних чисел a0, a1,...a(n-1). 
# Вивести всі j (1<=j<=n-2), для яких a(j-1)<a(j)<a(j+1).

seq=[int(input("Enter number: ")) for i in range(int(input("Enter length of sequence: ")))]
print("Your sequence:", seq)
print("j = ", [j for j in range(1, len(seq)-1) if seq[j-1]<seq[j] and seq[j]<seq[j+1]])

# OUTPUT SAMPLE:

# Enter length of sequence: 10
# Enter number: 1
# Enter number: 3
# Enter number: 5
# Enter number: 7
# Enter number: 9
# Enter number: -1
# Enter number: 0
# Enter number: 3
# Enter number: 10
# Enter number: 11
# Your sequence: [1, 3, 5, 7, 9, -1, 0, 3, 10, 11]
# j =  [1, 2, 3, 6, 7, 8]
