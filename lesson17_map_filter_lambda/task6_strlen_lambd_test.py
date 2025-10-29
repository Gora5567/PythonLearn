from task6_strlen_lambd import last_char

def test_last_char():
    test_cases = [
        {
            "in": "hello",
            "out": 5
        },
        {
            "in": "Python",
            "out": 6
        },
        {
            "in": "a",
            "out": 1
        },
        {
            "in": "12345",
            "out": 5
        },
        {
            "in": "",
            "out": 0
        },
    ]

    for case in test_cases:
        assert last_char(case["in"]) == case["out"]
