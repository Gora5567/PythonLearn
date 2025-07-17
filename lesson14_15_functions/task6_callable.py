from collections.abc import Iterable

def execute_if_iterable_and_callable(value):
    if not isinstance(value, Iterable) or isinstance(value, (str, bytes)):
        print("Переменная не является итерируемой.")
        return

    for item in value:
        if callable(item):
            try:
                result = item()
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"Ошибка при вызове: {e}")
