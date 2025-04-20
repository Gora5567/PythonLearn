import random


def start_task(a):
    print(f"\ntask {a} ---> start\n")


def end_task(a):
    print(f"\n\tend <--- task {a}\n")


def runner(func, *args):
    def wrapper(*args, **kwargs):
        start_task(func.__name__)
        func(*args, **kwargs)
        end_task(func.__name__)

    wrapper(args)


import random


def make_int_array(size: int) -> list[int]:
    return [random.randint(1, 100) for _ in range(size)]


def make_int_custom_array(size: int, from_: int, step: int) -> list[int]:
    # todo if step < 0 throw an exception
    some_list = list()

    for a in range(size):
        some_list.append(from_ + step * a)

    return some_list
