n_rows = int(input())

matrix = []
for rows in range(n_rows):
    data = list(input())
    matrix.append(data)


search_symbols = input()
possition = None
flag = False
for rows in range(n_rows):
    for cols in range(n_rows):
        if search_symbols == matrix[rows][cols]:
            possition = (rows, cols)
            flag = True
            break
    if flag:
        break

if possition:
    print(possition)
else:
    print(f"{search_symbols} does not occur in the matrix")







