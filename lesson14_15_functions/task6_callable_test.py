from task6_callable import execute_if_iterable_and_callable

def hello():
    return "hello!"

items = [hello, 52, "sss"]

def test_execute_if_iterable_and_callable():
    assert execute_if_iterable_and_callable(items) == "hello!"
