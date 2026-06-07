from collections import deque


kids = input().split()
n = int(input())

queue = deque(kids)

while True:
    if len(queue) == 1:
        break


    queue.rotate(-(n - 1))

    removed = queue.popleft()
    print(f"Removed {removed}")

print(f"Last is {queue[0]}")

