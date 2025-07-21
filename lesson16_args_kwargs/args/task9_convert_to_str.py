def convert_to_str(*args):
    res = []

    for arg in args:
        res.append(str(arg))

    return res


print(convert_to_str(1, 2, 3, True, ["Hello", "Foo"], {1: "goo", 5: "bye"}))
