def get_element(index, *args):
    if 0 <= index < len(args):
        return args[index]

    return None


print(get_element(0, 1, 2, 3))
print(get_element(5, 1, 2, 3))
