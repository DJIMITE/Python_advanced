clothes = list(map(int, input().split()))

max_capacity = int(input())

dress = 1
curent_sum = 0


while clothes:
    cloth = clothes.pop()

    if cloth + curent_sum <= max_capacity:
        curent_sum += cloth

    else:
        dress += 1
        curent_sum = cloth

print(dress)
