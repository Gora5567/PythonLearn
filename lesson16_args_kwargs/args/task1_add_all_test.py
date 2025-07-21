from task1_add_all import add_all


def test_add_all():
    assert add_all(1, 2, 3) == 6
    assert add_all(125, 225, 350) == 700
    assert add_all(123, 456, 789, 0) == 1368
