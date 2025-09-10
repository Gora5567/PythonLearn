def remove_keys(type_keys, **kwargs):
    res_dict = {k: v for k, v in kwargs.items() if k not in type_keys}
    return res_dict


print(remove_keys(['name'], name='jack', age=13, city='Odessa'))
