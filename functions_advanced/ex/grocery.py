def grocery_store(**kwargs):
    receipt = {}
    for key, value in kwargs.items():

        receipt[key] = value

    sort = sorted(receipt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = [f"{key}: {value}" for key, value in sort]
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
