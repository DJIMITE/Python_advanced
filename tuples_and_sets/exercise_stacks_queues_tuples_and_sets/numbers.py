first_number = set(map(int, input().split()))
second_number = set(map(int, input().split()))

n = int(input())

for i in range(n):
    line = input().split()
    command = line[0] + " " + line[1]

    if command == "Add First":
        number = line[2:]
        for i in number:
            first_number.add(int(i))
    elif command == "Add Second":
        number = line[2:]
        for i in number:
            second_number.add(int(i))
    elif command == "Remove First":
        number = line[2:]
        for i in number:
            if int(i) in first_number:
                first_number.remove(int(i))
    elif command == "Remove Second":
        number = line[2:]
        for i in number:
            if int(i) in second_number:
                second_number.remove(int(i))
    elif command == "Check Subset":
        if first_number.issubset(second_number) or second_number.issubset(first_number):
            print("True")
        else:
            print("False")
print(", ".join(map(str,sorted(first_number))))
print(", ".join(map(str, sorted(second_number))))