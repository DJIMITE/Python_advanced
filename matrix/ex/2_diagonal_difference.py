n = int(input())

matrix = []
diagonals = []
secondary_diagonal = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    diagonals.append(matrix[i][i])

for i in range(n):
    secondary_diagonal.append(matrix[i][n - 1 - i])

sum_diagonal = sum(diagonals)
sum_secondary_diagonal = sum(secondary_diagonal)

print(abs(sum_diagonal - sum_secondary_diagonal))




