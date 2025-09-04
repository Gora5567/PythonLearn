from task11_plus10 import plus_ten

def test_plus_ten():
    test_cases = [
        {"in": [1, 2, 3], "out": [11, 12, 13]},
        {"in": [0, -5, 10], "out": [10, 5, 20]},
    ]
    for case in test_cases:
        assert plus_ten(case["in"]) == case["out"]
