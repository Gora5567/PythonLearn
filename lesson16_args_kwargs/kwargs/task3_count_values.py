def count_values(**kwargs):
    key_count = 0
    for key in kwargs:
        key_count += 1

    return key_count

print(count_values(name='Jack', age=20))