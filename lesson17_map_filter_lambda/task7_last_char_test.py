from task7_last_char import last_char


def test_last_char():
    assert last_char("apple") == "e"
    assert last_char("father") == "r"
    assert last_char("yehor") == "r"
