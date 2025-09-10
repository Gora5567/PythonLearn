def count_values(**kwargs):
    return len(kwargs.keys())

    # key_count = 0
    # for _ in kwargs:
    #     key_count += 1
    #
    # return key_count


print(count_values(name='Jack', age=20))
