from task16_transfer import nums_to_strings

def test_nums_to_strings():
    assert nums_to_strings([1, 2, 3]) == ["1", "2", "3"]
    assert nums_to_strings([10, 20]) == ["10", "20"]
    assert nums_to_strings([]) == []
