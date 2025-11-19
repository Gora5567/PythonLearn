from task6_filter_by_value_type import filter_by_value_type


def test_filter_by_value_type():
    assert (filter_by_value_type(str, first="hello", second=2)
            == {"first": "hello"})
    assert (filter_by_value_type(int, first="hello", second=2)
            == {"second": 2})
    assert (filter_by_value_type(bool, first="hello", second=2)
            == {})
