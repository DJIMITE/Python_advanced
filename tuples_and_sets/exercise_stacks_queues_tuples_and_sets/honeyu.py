from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:

    current_bee = bees[0]
    current_nectar = nectar[-1]

    # ако нектарът не стига
    if current_nectar < current_bee:
        nectar.pop()
        continue

    # достатъчно нектар
    symbol = symbols.popleft()

    if symbol == "+":
        result = current_bee + current_nectar

    elif symbol == "-":
        result = current_bee - current_nectar

    elif symbol == "*":
        result = current_bee * current_nectar

    elif symbol == "/":
        if current_nectar == 0:
            bees.popleft()
            nectar.pop()
            continue
        result = current_bee / current_nectar

    total_honey += abs(result)

    bees.popleft()
    nectar.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")