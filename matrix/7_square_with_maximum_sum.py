import sys
n_rows, n_cols = map(int, input().split(", "))

matrix = []

for _ in range(n_rows):
    data = list(map(int, input().split(", ")))
    matrix.append(data)
max_sum = -sys.maxsize
index_max_sum = None
for row in range(n_rows- 1):
    for col in range(n_cols- 1):
        one = matrix[row][col]
        two = matrix[row][col+1]
        three = matrix[row+ 1][col]
        four = matrix[row+1][col+1]
        current_sum = one + two + three + four

        if current_sum > max_sum:
            max_sum = current_sum
            index_max_sum = [[one, two],
                             [three, four]]

print(*index_max_sum[0])
print(*index_max_sum[1])
print(max_sum)





