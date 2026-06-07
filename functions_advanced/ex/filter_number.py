def even_odd_filter(**kwargs):
    even_odd = {}
    for key, values in kwargs.items():
        if key == "even":
            even_odd[key] = [x for x in values if x % 2 == 0]
        elif key == "odd":
            even_odd[key] = [x for x in values if x % 2 != 0]

    return dict(sorted(even_odd.items(), key=lambda x: x[1], reverse=True))
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
