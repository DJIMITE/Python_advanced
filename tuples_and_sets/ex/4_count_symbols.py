text = input()

count_symbols = {}

for char in text:
    if char not in count_symbols:
        count_symbols[char] = 0
    count_symbols[char] += 1

for key, value in sorted(count_symbols.items()):
    print(f"{key}: {value} time/s")