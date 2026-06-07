def age_assignment(*args, **kwargs):
    result = []
    for arg in args:
        if arg[0] in kwargs:
            result.append(f"{arg} is {kwargs[arg[0]]} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))


