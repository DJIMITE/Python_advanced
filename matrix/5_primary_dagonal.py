n_rows = int(input())

matrix = []

for rows in range(n_rows):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)
sums = 0
for rows in range(n_rows):
    sums += matrix[rows][rows]

print(sums)
