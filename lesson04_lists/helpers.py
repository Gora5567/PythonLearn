def start_task():
    print("\ntask---> start\n")


def end_task():
    print("\n\tend <---task\n")


def run(func):
    start_task()
    func()
    end_task()
    print("\n")
