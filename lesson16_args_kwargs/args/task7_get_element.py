def get_element(index, *args):
    if 0 <= index < len(args):
        return args[index]

    return None
