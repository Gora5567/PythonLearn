from task7_sum_numeric_values import sum_numeric_values


def test_sum_numeric_values():
    assert sum_numeric_values(first="hello", second=2, third=10) == 12
    assert sum_numeric_values(first="hello", second="2", third=10) == 10
    assert sum_numeric_values(first="hello", second="2", third="10") == 0
