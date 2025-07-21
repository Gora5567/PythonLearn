from task3_count_args import count_args


def test_count_args():
    assert count_args(1, 2, 3, 78, 43508, 12309) == 6
    assert count_args(5, 7, 8, 87) == 4
    assert count_args("yo", 4345, "bye bye") == 3
