number = tuple(float(i) for i in input().split())

data = {}
for x in number:

    if x not in data:
        data[x] = number.count(x)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")





