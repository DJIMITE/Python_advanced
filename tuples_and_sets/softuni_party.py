n = int(input())

party = set()

for i in range(n):
    people = input()

    party.add(people)

while True:
    command = input()
    if command == "END":
        break

    if command in party:
        party.remove(command)
sorted_aptry = sorted(party)
print(len(party))
for name in sorted_aptry:
    print(name)