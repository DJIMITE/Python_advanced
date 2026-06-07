n_rows, n_cols = list(map(int, input().split(", ")))
matrix = []
sum_all = 0
for row in range(n_rows):
    numbers = list(map(int, input().split(", ")))
    sum_all += sum(numbers)
    matrix.append(numbers)
print(sum_all)
print(matrix)
