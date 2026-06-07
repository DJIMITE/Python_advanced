def negative_positive(*args):
    negative_num = sum([x for x in args if x < 0])
    positive_num = sum([j for j in args if j > 0])

    if abs(negative_num) > positive_num:
        return f'{negative_num}\n{positive_num}\nThe negatives are stronger than the positives'
    else:
        return f'{negative_num}\n{positive_num}\nThe positives are stronger than the negatives'


numbers = [int(x) for x in input().split()]
result = negative_positive(*numbers)
print(result)