number = input().split()

stack_num = []

for i in range(len(number)):
    stack_num.append(number.pop())

print(" ".join(stack_num))