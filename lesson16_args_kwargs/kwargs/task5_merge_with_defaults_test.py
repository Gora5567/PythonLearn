from task5_merge_with_defaults import merge_with_defaults


def test_merge_with_defaults():
    kwargs = {"name": "jack", "car": "bmw"}
    test_cases = [
        {
            "in": {"greetings": "hello", "gender": "male"},
            "out": {"greetings": "hello", "gender": "male",
                    "name": "jack", "car": "bmw"},
        },
        {
            "in": 1,
            "out": {"name": "jack", "car": "bmw"},
        }
    ]

    for case in test_cases:
        assert merge_with_defaults(case["in"], **kwargs) == case["out"]
