from collections import deque
food_day = int(input())

max_num = 0
food = input().split()
queue = deque()

for i in range(len(food)):
    queue.append(food[i])
    if max_num < int(food[i]):
        max_num = int(food[i])


print(max_num)

while queue:
    curent_queue = int(queue[0])

    if curent_queue <= food_day:
        food_day -= curent_queue
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(queue)}")



