def filter_by_value_type(required_type, **kwargs):
    res = {}
    for key, value in kwargs.items():
        if type(value) is required_type:
            res.update({key: value})
    return res

print(filter_by_value_type(str, first="hello", second=2))