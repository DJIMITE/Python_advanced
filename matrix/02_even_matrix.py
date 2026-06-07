n_rows = int(input())
matrix = []
for row in range(n_rows):
    numbers = [int(i) for i in input().split(", ") if int(i) % 2 == 0]
    matrix.append(numbers)

print(matrix)