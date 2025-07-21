from task9_convert_to_str import convert_to_str


def test_convert_to_str():
    assert convert_to_str(1, 2, 3) == ["1", "2", "3"]
    assert convert_to_str(True, False) == ["True", "False"]
    assert convert_to_str([1, 2], ["a", "b"]) == ["[1, 2]", "['a', 'b']"]
