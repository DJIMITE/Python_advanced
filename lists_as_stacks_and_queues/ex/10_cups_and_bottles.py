from collections import deque

cups = deque(map(int, input().split()))

bottles = list(map(int, input().split()))
wasted_litters_of_water = 0
flag = True
while True:
    if len(cups)  == 0:
        break
    if len(bottles) == 0:
        flag = False
        break
    bottles_one = bottles.pop()
    cups_one = cups[0]


    if bottles_one >= cups_one:

        wasted_litters_of_water += bottles_one - cups_one
        cups[0] -= bottles_one
    else:
        cups[0] -= bottles_one

    if cups[0] <= 0:
        cups.popleft()



if flag:
    print(f"Bottles: {' '.join(map(str, bottles))}")
    print(f"Wasted litters of water: {wasted_litters_of_water}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {wasted_litters_of_water}")