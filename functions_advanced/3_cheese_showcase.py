def sorting_cheeses(**kwargs):
    result_Sort = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result= ""
    for key, values in result_Sort:
        result += f"{key}\n"
        for value in sorted(values, reverse=True):
            result += f"{value}\n"
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
