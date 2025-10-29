from task14_filter_a import filter_a

def test_filter_a():
    test_cases = [
        {"in": ["apple", "banana", "apricot", "cherry"], "out": ["apple", "apricot"]},
        {"in": ["dog", "cat"], "out": []},
    ]
    for case in test_cases:
        assert filter_a(case["in"]) == case["out"]
