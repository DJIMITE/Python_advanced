from collections import deque

robots_input = input().split(";")

robots = []

for i in robots_input:
    name_robots, time = i.split("-")

    robots.append({
        "name":name_robots,
        "time": time,
        "free_at": 0
    })

h, m, s = map(int, input().split(":"))

current_time = h * 3600 + m * 60 + s

products = deque()

while True:
    line = input()

    if line == "End":
        break
    products.append(line)

while products:
    current_time += 1
    current_product = products.popleft()

    is_taken = False
    for i in robots:

        if i["free_at"] <= current_time:
            i["free_at"] = current_time + int(i["time"])

            hrs = (current_time // 3600) % 24
            mins = (current_time // 60) % 60
            secs = current_time % 60

            print(f"{i['name']} - {current_product} [{hrs:02d}:{mins:02d}:{secs:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)

