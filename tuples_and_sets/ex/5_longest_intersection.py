n = int(input())

longest = set()

for _ in range(n):
    data_1, data_2 = input().split("-")

    first_start, first_end = map(int, data_1.split(","))
    second_start, second_end = map(int, data_2.split(","))

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    intersection = first.intersection(second)

    if len(intersection) > len(longest):
        longest = intersection

print(f"Longest intersection is [{', '.join(map(str, longest))}] with length {len(longest)}")
