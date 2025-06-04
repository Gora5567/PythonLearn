from collections.abc import Iterable
from collections.abc import Callable


def execute_if_iterable_and_callable(value):
    if !isinstance(value, Iterable) or isinstance(value, (str, bytes)):
        print("Переменная не является итерируемой.")
        return 
        
    for item in value:
        if !callable(item):
            continue
                
        try:
            item()
        except Exception as e:
            print(f"Ошибка при вызове: {e}")
