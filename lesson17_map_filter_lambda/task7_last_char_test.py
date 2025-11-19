from task7_last_char import last_char


def test_last_char():
    test_cases = [
        {"in": "hello", "out": "o"},
        {"in": "Python", "out": "n"},
        {"in": "a", "out": "a"},
        {"in": "12345", "out": "5"},
    ]

    for case in test_cases:
        assert last_char(case["in"]) == case["out"]
