from task4_filter_positive import filter_positive


def test_filter_positive():
    assert filter_positive([1, -2, 3, 0, -5, 10]) == [1, 3, 10]
    assert filter_positive([-1, -2, -3]) == []
    assert filter_positive([0, 0, 0]) == []
    assert filter_positive([5, 15, 25]) == [5, 15, 25]
    assert filter_positive([]) == []
