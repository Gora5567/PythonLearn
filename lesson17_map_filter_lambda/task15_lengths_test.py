from task15_lengths import lengths

def test_lengths():
    test_cases = [
        {"in": ["apple", "banana", "apricot", "cherry"], "out": [5, 6, 7, 6]},
        {"in": ["a", "bb", "ccc"], "out": [1, 2, 3]},
    ]
    for case in test_cases:
        assert lengths(case["in"]) == case["out"]
