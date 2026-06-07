n, m = list(map(int, input().split()))
n_number = set()
m_number = set()
for i in range(n):
    n_number.add(int(input()))

for x in range(m):
    m_number.add(int(input()))


result = n_number & m_number

for num in result:
    print(num)

