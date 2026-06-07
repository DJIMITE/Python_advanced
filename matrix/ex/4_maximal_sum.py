import sys
rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

all_sum = -sys.maxsize
all_sum_index = []
for row in range(rows- 2):
    for col in range(cols- 2):
        one = matrix[row][col]
        two = matrix[row][col+1]
        three = matrix[row][col+2]
        four = matrix[row + 1][col]
        five = matrix[row + 1][col + 1]
        six = matrix[row + 1][col + 2]
        seven = matrix[row + 2][col]
        eight = matrix[row + 2][col + 1]
        nine = matrix[row + 2][col + 2]
        currnt_sum = one + two + three + four + five + six + seven + eight + nine

        if currnt_sum > all_sum:
            all_sum = currnt_sum
            all_sum_index = [
                [one, two, three],
                [four, five, six],
                [seven, eight, nine]
            ]



print(f"Sum = {all_sum}")
for index in all_sum_index:
    print(*index)

