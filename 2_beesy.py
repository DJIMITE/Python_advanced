n = int(input())

energy = 15
min_nectar = 30
bee_r, bee_c = 0, 0
matrix = []
nectar = 0
recovery_energy = False
for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "B":
            bee_r, bee_c = i, j
            matrix[i][j] = "-"


def command_move(r, c, command):
    if command == "up":
        r = (r - 1) % n
    elif command == "down":
        r = (r + 1) % n
    elif command == "left":
        c = (c - 1) % n
    elif command == "right":
        c = (c + 1) % n
    return r, c

while True:
    energy -= 1
    command = input()
    r, c = command_move(bee_r, bee_c, command)
    bee_r, bee_c = r, c

    if matrix[r][c].isdigit():
        nectar += int(matrix[r][c])
        matrix[r][c] = "-"
    elif matrix[r][c] == "H":
        if nectar >= min_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            bee_r, bee_c = r, c
            break
        else:
            print("Beesy did not manage to collect enough nectar.")
            bee_r, bee_c = r, c
            break
    if not recovery_energy and energy <= 0:
        if nectar >= min_nectar:
            recovery = nectar - min_nectar
            energy += recovery
            recovery_energy = True
            nectar = 30

    if energy <= 0:
        print("This is the end! Beesy ran out of energy.")
        bee_r, bee_c = r, c
        break


matrix[bee_r][bee_c] = "B"

for i in matrix:
    print("".join(i))