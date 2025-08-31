from task8_sorted import *

def test_sorted():
    test_cases = [
        {
            "in": ["laptop", "beach", "cinema", "greeting"],
            "out": ["beach", "laptop", "cinema", "greeting"],
        },
        {
            "in": ["League of Legends", "Fortnite", "Apex Legends"],
            "out": ["Fortnite", "Apex Legends", "League of Legends"],
        }
    ]

    for case in test_cases:
        assert for_sorted_list(case["in"]) == case["out"]
