from task7_get_element import get_element


def test_get_element():
    assert get_element(0, 1, 2, 3) == 1
    assert get_element(3, 1, 2, 3) is None
    assert get_element(2, 1, 2, 3) == 3
