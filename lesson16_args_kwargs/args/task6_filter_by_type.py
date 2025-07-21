def filter_by_type(required_type, *args):
    res = []

    for number in args:
        if type(number) is required_type:
            res.append(number)

    return res


print(filter_by_type(int, 1, 2, 3, "hello", True))
