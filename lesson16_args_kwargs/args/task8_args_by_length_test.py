from task8_args_by_length import args_by_length


def test_args_by_length():
    assert (args_by_length(3, "hi", 7890, True, "Hi, my name is", "Bye bye")
            == ["Hi, my name is", "Bye bye"])
    assert (args_by_length(1, "hi", 7890, True, "Hi, my name is", "Bye bye")
            == ["hi", "Hi, my name is", "Bye bye"])
    assert (args_by_length(1000, "hi", 7890, True, "Hi, my name is", "Bye bye")
            == [])
