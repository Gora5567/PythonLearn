def sum_numeric_values(**kwargs):
    required_type = int
    count = 0

    for key, value in kwargs.items():
        if type(value) is required_type:
            count += value

    return count


print(sum_numeric_values(first="hello", second=2, third=10))
