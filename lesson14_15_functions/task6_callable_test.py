import sys
import io
from task6_callable import execute_if_iterable_and_callable


def test_execute_if_iterable_and_callable():
    def capture_output(value):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            execute_if_iterable_and_callable(value)
        finally:
            sys.stdout = old_stdout
        return buffer.getvalue().strip()

    def hello():
        print("hello!", end='')

    def hello2():
        print("hello2", end='')

    def yo():
        print("yo!", end='')

    items = [hello, 52, "sss"]
    items2 = [hello, 52, hello2]
    items3 = [hello2, hello, yo, "sss"]

    assert capture_output(items) == "hello!"
    assert capture_output(items2) == "hello!hello2"
    assert capture_output(items3) == "hello2hello!yo!"
