# 12.	Дано матрицю A розмірності n*n  і вектор x  розмірності n . Непарні стрічки матриці A  замінити на вектор x.


n=int(input("Enter number of rows/columns: "))

matrix=[list(map(int, input("(matr) Enter row: ").split())) for i in range(n)]
vector=list(map(int, input("(vec) Enter row: ").split()))
matrix=list([vector if i%2==0 else matrix[i] for i in range(n)])

print(matrix)



# OUTPUT SAMPLE:
# Enter number of rows/columns: 5
# (matr) Enter row: 1 2 3 4 5
# (matr) Enter row: 4 5 6 7 8
# (matr) Enter row: 3 4 7 3 1
# (matr) Enter row: 4 5 6 9 7
# (matr) Enter row: 1 2 3 4 3
# (vec) Enter row: 0 0 0 0 0
# [[0, 0, 0, 0, 0], [4, 5, 6, 7, 8], [0, 0, 0, 0, 0], [4, 5, 6, 9, 7], [0, 0, 0, 0, 0]]


# via Numpy:

import numpy

n=int(input("Enter number of rows/columns: "))

matrix=numpy.full((n,n), 3)
vector=numpy.full(n, 0)
for i in range(n):
    if i%2==0:
        matrix[i]=vector
print(matrix)

# OUTPUT SAMPLE:
# Enter number of rows/columns: 5
# [[0 0 0 0 0]
#  [3 3 3 3 3]
#  [0 0 0 0 0]
#  [3 3 3 3 3]
#  [0 0 0 0 0]]