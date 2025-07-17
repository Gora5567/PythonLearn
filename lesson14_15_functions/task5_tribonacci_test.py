from task5_tribonacci import tribonacci

def test_tribonacci():
    assert tribonacci(-5) == []
    assert tribonacci(0) == []
    assert tribonacci(1) == [0]
    assert tribonacci(2) == [0, 1]
    assert tribonacci(3) == [0, 1, 1]
    assert tribonacci(4) == [0, 1, 1, 2]
    assert tribonacci(5) == [0, 1, 1, 2, 4]