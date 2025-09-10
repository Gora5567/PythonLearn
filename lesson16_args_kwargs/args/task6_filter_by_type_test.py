import sys
import io
from task6_filter_by_type import filter_by_type

def test_filter_by_type():
    assert filter_by_type(int, 1, 2, 3, "hello", True) == [1, 2, 3]
    assert filter_by_type(bool, 1, 2, 3, "hello", True) == [True]
    assert filter_by_type(str, 1, 2, 3, "hello", True) == ["hello"]