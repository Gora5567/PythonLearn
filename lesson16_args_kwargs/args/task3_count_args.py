def count_args(*args):
    count = 0

    for _ in args:
        count += 1

    return count


print(count_args(1, 2, 3, 78, 43508, 12309))
