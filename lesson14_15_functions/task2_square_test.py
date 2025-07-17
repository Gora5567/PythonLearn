from task2_square import square

def test_square():
    test_cases = {
        2: 4,
        4: 16,
        6: 36,
        8: 64,
        10: 100,
    }

    for k, v in test_cases.items():
        assert square(k) == v
