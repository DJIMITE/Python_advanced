line = input()


stack = []
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
flag = True
for ch in line:

    if ch in "({[":
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch] :
            flag = False
            break

if flag and not stack:
    print("YES")
else:
    print("NO")

