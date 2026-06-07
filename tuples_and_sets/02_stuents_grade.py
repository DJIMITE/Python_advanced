n = int(input())
all_students = {}
for i in range(n):
    commad = input().split()
    student = commad[0]
    grade = commad[1]

    if student not in all_students:
        all_students[student] = []
    all_students[student].append(float(grade))

for key, value in all_students.items():
    avg = sum(value) / len(value)
    print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {f'{avg:.2f}'})")


