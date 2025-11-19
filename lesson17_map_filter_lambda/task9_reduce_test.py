from task9_reduce import product_list


def test_product_list():
    test_cases = [
        {
            "in": [1, 2, 3, 4],
            "out": 24,
        },
        {
            "in": [5, 5, 2],
            "out": 50,
        },
        {
            "in": [10],
            "out": 10,
        }
    ]

    for case in test_cases:
        assert product_list(case["in"]) == case["out"]
