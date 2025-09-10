def args_by_length(n, *args):
    res = []

    for arg in args:
        if type(arg) == str and len(arg) > n:
            res.append(arg)

    return res
