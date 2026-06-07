from collections import deque
price_bullet = int(input())

the_size_weapon = int(input())

bullets = list(map(int, input().split()))

keys = deque()

key = input().split()
all_money = int(input())
for i in key:
    keys.append(int(i))

fire = 0
current_fire =0
reloading = 0
while True:
    if len(keys) == 0 or len(bullets) == 0:
        break
    fire += 1
    current_fire += 1
    bullet = bullets[-1]
    strike_key = keys[0]



    if bullet <= strike_key:
        keys.popleft()
        bullets.pop()
        print("Bang!")

    else:
        print("Ping!")
        bullets.pop()

    if current_fire >= the_size_weapon and len(bullets) > 0:
        print("Reloading!")
        current_fire = 0
        reloading += 1


if len(keys) == 0:
    print(f"{len(bullets)} bullets left. Earned ${all_money - fire * price_bullet}")

else:
    print(f"Couldn't get through. Locks left: {len(keys)}")







