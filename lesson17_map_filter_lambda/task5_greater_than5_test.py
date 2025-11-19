from task5_greater_than5 import greater_than5_list


def test_greater_than5():
    test_cases = [
        {
            "in": [1, 2, 3, 8, 6],
            "out": [8, 6]
        },
        {
            "in": [10, 10000, 3, 1.7, 5],
            "out": [10, 10000],
        }
    ]

    for case in test_cases:
        assert greater_than5_list(case["in"]) == case["out"]
