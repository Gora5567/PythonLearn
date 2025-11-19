from task17_sorted_last import sort_by_last_letter


def test_sort_by_last_letter():
    words = ['car', "yeah", "foo", "goo"]
    assert sort_by_last_letter(words) == ['yeah', 'foo', 'goo', 'car']
    assert sort_by_last_letter(["a", "b"]) == ["a", "b"]
