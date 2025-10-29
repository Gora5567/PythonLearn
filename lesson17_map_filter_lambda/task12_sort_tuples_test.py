from task12_sort_tuples import sort_by_second

def test_sort_by_second():
    test_cases = [
        { "in": [(1, 5), (3, 2), (2, 8)],
         "out": [(3, 2), (1, 5), (2, 8)]},

        { "in": [(5, 10), (1, -1)],
         "out": [(1, -1), (5, 10)]},
    ]
    for case in test_cases:
        assert sort_by_second(case["in"]) == case["out"]
