from functools import reduce

def sum_numbers(*args):
    return sum(args)

def sub_number(*args):
    return reduce(lambda x, y: x - y, args)

def mul_number(*args):
    return reduce(lambda x, y: x * y, args)

def div_number(*args):
    return reduce(lambda x, y: x / y, args)

def operate(operator, *args):
    result = mapper[operator]
    return result(*args)

mapper = {
    "+": sum_numbers,
    "-": sub_number,
    "*": mul_number,
    "/": div_number,
}
print(operate("*", 3, 4))
