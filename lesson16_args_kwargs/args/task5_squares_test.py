from task5_squares import squares


def test_squares():
    assert list(squares(4, 5, 6)) == [16, 25, 36]
    assert list(squares(1, 2, 3, 4)) == [1, 4, 9, 16]
    assert list(squares(7, 8, 9, 10)) == [49, 64, 81, 100]
