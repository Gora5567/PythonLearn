from task4_square_map import square_list

def test_square_lambd_map():
    test_cases = [
        {
            "in": [1, 2, 3, 4, 5],
            "out": [1, 4, 9, 16, 25],
        },
        {
            "in": [6, 7, 8, 9, 10],
            "out": [36, 49, 64, 81, 100],
        }
    ]

    for case in test_cases:
        assert square_list(case["in"]) == case["out"]
