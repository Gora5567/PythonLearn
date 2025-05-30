from collections.abc import Iterable
from collections.abc import Callable


def execute_if_iterable_and_callable(value):
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
        for item in value:
            if callable(item):
                try:
                    item()
                except Exception as e:
                    print(f"Ошибка при вызове: {e}")
    else:
        print("Переменная не является итерируемой.")
