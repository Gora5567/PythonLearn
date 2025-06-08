from task6_callable import execute_if_iterable_and_callable
def hello():
    print("hello!")

items = [hello, 52, "sss"]

execute_if_iterable_and_callable(items)