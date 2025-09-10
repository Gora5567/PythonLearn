from task2_find_max import find_max


def test_find_max():
    assert find_max(1, 2, 3) == 3
    assert find_max(125, 225, 350) == 350
    assert find_max(123, 456, 789, 0) == 789
