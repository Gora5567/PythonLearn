class Counter:
    total_created = 0  # атрибут класса

    def __init__(self):
        Counter.total_created += 1
