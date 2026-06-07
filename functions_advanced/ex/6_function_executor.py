def func_executor(*args):
    result = []
    for funcion, argumnets in args:
        number = funcion(*argumnets)

        result.append(f"{funcion.__name__} - {number}")

    return "\n".join(result)



def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

