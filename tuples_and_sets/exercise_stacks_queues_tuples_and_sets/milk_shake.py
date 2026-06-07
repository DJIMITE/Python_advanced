from collections import deque

chocolate = list(map(int,input().split(", ")))
milk_cup = deque(map(int, input().split(", ")))

milk_shake = 0
while True:

    if len(chocolate) == 0 or len(milk_cup) == 0 or milk_shake == 5:
        break


    if chocolate[-1] >= 0:
        chocolate.pop()
    if milk_cup[0] >= 0:
        milk_cup.popleft()

    one_cup_chocolate = chocolate[-1]
    one_cup_milk = milk_cup[0]

    if one_cup_chocolate == one_cup_milk:
        milk_shake += 1
        chocolate.pop()
        milk_cup.popleft()
    else:
        milk_cup.append(milk_cup.popleft())
        chocolate[-1] -= 5

if milk_shake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
    if len(chocolate) == 0:
        print("empty")
    else:
        print(", ".join(map(str,chocolate)))

    if len(milk_cup) == 0:
        print("empty")
    else:
        print(", ".join(map(str, milk_cup)))
else:
    print("Not enough chocolate")
    if len(chocolate) == 0:
        print("empty")
    else:
        print(", ".join(map(str,chocolate)))

    if len(milk_cup) == 0:
        print("empty")
    else:
        print(", ".join(map(str, milk_cup)))
