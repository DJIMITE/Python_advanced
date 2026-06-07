from  collections import deque
n = int(input())

pumps = deque()

for i in range(n):
    fuel, distance= list(map(int, input().split()))
    pumps.append((fuel, distance))

start_index = 0

while True:
    tank = 0
    flag = True

    for fuel, distance in pumps:
        tank += fuel
        tank -= distance

        if tank < 0:
            flag = False
            break

    if flag:
        print(start_index)
        break
    start_index += 1
    pumps.append(pumps.popleft())





