from task2_add import add

def test_add():
    assert add(1, 2) == 3
    assert add(10, 2) == 12
    assert add(5, 2.5) == 7.5