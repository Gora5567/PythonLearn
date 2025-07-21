def args_by_length(n, *args):
    res = []

    for arg in args:
        if type(arg) == str and len(arg) >= n:
            res.append(arg)

    return res


print(args_by_length(5, "ffsdfsdfdsfsf", "fgdjjjjjj", "ff", 1, 45645, True, ["yofdgdfgdfgdgdf", 546, True]))
