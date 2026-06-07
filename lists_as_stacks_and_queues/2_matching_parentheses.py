text = input()

idx = []

for i in range(len(text)):

    if text[i] == "(":
        idx.append(i)
    elif text[i] == ")":
        start_idx = idx.pop()
        end_idx = i
        print(text[start_idx:end_idx + 1])