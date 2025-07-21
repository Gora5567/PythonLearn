from task10_calculate import calculate

def test_calculate():
    assert calculate("+", 8, 8, 8) == 24
    assert calculate("*", 8, 8) == 64