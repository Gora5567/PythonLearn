def squares(*args):
    res = []

    for arg in args:
        res.append(arg ** 2)

    return res


print(squares(4, 5, 6))
