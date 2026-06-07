from collections import deque
liters_water = int(input())

water_tail = deque()
while True:

    people = input()

    if people == "Start":
        break
    else:
        water_tail.append(people)

while True:
    command = input()


    if command == "End":
        print(f"{liters_water} liters left")
        break

    elif "refill" in command:
        lietrs = command.split()

        liters_water += int(lietrs[1])
    else:
        if command.isdigit():
            if int(command) <= liters_water:
                liters_water -= int(command)
                print(f"{water_tail.popleft()} got water")
            else:
                print(f"{water_tail.popleft()} must wait" )
