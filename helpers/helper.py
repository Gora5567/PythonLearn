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
