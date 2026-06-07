from operator import index

n = int(input())

matrix = []
diagonals = []
secondary_diagonal = []
for i in range(n):
    matrix.append(list(map(int, input().split(", "))))


for i in range(n):
        diagonals.append(matrix[i][i])
inedx = -1
for j in range(n):
        secondary_diagonal.append(matrix[j][inedx])
        inedx -= 1
print(f"Primary diagonal: {', '.join(map(str, diagonals))}. Sum: {sum(diagonals)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")

