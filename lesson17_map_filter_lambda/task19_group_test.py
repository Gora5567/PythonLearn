from task19_group import *
def test_group_by_first_letter():
    words = ["apple", "apricot", "banana", "blueberry", "cherry", "cranberry"]
    expected = {
        'a': ['apple', 'apricot'],
        'b': ['banana', 'blueberry'],
        'c': ['cherry', 'cranberry']
    }
    assert group_by_first_letter(words) == expected