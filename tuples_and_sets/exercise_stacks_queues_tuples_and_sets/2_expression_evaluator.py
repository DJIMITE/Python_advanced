line = input().split()

numbers = []
play = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,

}
for command in line:

    if command not in "+-*/":
        numbers.append(int(command))
    else:
        while numbers > 1:
            num_one = numbers.pop()
            num_two = numbers.pop()
            numbers.append(play[command](num_one, num_two))
print(", ".join(map(str,numbers)))
