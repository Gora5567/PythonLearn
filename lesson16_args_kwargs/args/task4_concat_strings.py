def concat_strings(*args):
    concat = ""

    for arg in args:
        concat = concat + arg

    return concat


print(concat_strings("hi", "my name is yehor"))
