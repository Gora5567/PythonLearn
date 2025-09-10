def has_key(key, **kwargs):
    return key in kwargs

    # if key in kwargs:
    #     return True
    # else:
    #     return None


print(has_key('smth', name='Jack', age=20))
