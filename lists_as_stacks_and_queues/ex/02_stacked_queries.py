n = int(input())
stack_num = []
for i in range(n):
    command = input().split()

    if command[0] == "1":
        num = int(command[1])
        stack_num.append(num)
    elif command[0] == "2":
        if stack_num:
            stack_num.pop()
    elif command[0] == "3":
        if stack_num:
            print(max(stack_num))
    elif command[0] == "4":
        if stack_num:
            print(min(stack_num))


print(", ".join(str(x) for x in reversed(stack_num)))


#
# n = int(input())
# stack = []
#
# for _ in range(n):
#     command = input().split()
#
#     if command[0] == "1":
#         number = int(command[1])
#         stack.append(number)
#
#     elif command[0] == "2":
#         if stack:
#             stack.pop()
#
#     elif command[0] == "3":
#         if stack:
#             print(max(stack))
#
#     elif command[0] == "4":
#         if stack:
#             print(min(stack))
#
# # Print stack from top to bottom
# print(", ".join(str(x) for x in reversed(stack)))

