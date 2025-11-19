from task13_age_check import age_check


def test_age_check():
    test_cases = [
        {"in": 20, "out": "adult"},
        {"in": 15, "out": "child"},
        {"in": 18, "out": "adult"},
    ]
    for case in test_cases:
        assert age_check(case["in"]) == case["out"]
