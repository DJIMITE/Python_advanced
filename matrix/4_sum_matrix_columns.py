n_rows, n_cols = map(int, input().split(", "))

matrix = []

for i in range(n_rows):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

for cols in range(n_cols):
    sum_cols = 0
    for rows in range(n_rows):
        sum_cols += matrix[rows][cols]
    print(sum_cols)
