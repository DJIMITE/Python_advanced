n = int(input())
elements = set()
for i in range(n):
    element = input().split()
    for j in element:
        elements.add(j)

for x in elements:
    print(x)
