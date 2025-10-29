from task10_palindrome import is_palindrome

def test_is_palindrome():
    test_cases = [
        {"in": "level", "out": True},
        {"in": "hello", "out": False},
        {"in": "madam", "out": True},
    ]
    for case in test_cases:
        assert is_palindrome(case["in"]) == case["out"]
