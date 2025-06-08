from task6_callable import execute_if_iterable_and_callable
def hello():
    print("Привет!")

items = [hello, 52, "ыыы"]

execute_if_iterable_and_callable(items)