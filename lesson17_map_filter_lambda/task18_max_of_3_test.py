from task18_max_of_3 import max_of_three

def test_max_of_three():
    assert max_of_three(3, 7, 5) == 7
    assert max_of_three(10, 2, 5) == 10
    assert max_of_three(-1, -5, -3) == -1
