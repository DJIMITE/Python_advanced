row, col = map(int, input().split())

matrix = []

for _ in range(row):
    matrix.append(list(input().split()))
count = 0
for i in range(row- 1):
    for j in range(col-1):
        one = matrix[i][j]
        two = matrix[i][j+1]
        three = matrix[i+1][j]
        four = matrix[i+1][j+1]

        if one == two ==  three == four:
            count += 1

print(count)


