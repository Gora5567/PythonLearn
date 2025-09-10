from task4_concat_strings import concat_strings


def test_concat_strings():
    assert concat_strings("yo", "my name is Yehor") == "yomy name is Yehor"
    assert concat_strings("im13", "wau?") == "im13wau?"
