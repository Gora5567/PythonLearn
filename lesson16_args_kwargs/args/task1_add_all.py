def add_all(*args):
    all = 0

    for number in args:
        all = all + number

    return all


print(add_all(10, 20, 2, 1, 4))
