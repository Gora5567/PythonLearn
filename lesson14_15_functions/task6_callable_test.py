from task6_callable import execute_if_iterable_and_callable

def test_execute_if_iterable_and_callable():
    def hello():
        return "hello!"
    def hello2():
        return "hello2"

    items = [hello, 52, "sss"]
    items2 = [hello2, 52, hello2]

    assert execute_if_iterable_and_callable(items) == "hello!"
    assert execute_if_iterable_and_callable(items) == "hello!"

