from string import punctuation
with open("text.txt") as f:
    f = f.readlines()
    result = []

    for row, line in enumerate(f):
        count_alpha = 0
        count_punctuation = 0
        for char in line:
            if char.isalpha():
                count_alpha += 1
            if char in punctuation:
                count_punctuation += 1

        result.append(f"Line {row + 1}: {line.strip()} ({count_alpha})({count_punctuation})")

with open("text.txt", "w") as f:
    f.write("\n".join(result))


