n_rows = int(input())
matrix = []
for row in range(n_rows):
    numbers = list(map(int, input().split(", ")))
    matrix.extend(numbers)
print(matrix)

