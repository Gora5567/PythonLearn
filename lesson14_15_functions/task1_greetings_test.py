import sys
import io
from task1_greetings import greetings

def test_greetings():

    def output(name):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        try:
            greetings(name)
        finally:
            sys.stdout = old_stdout

        return buffer.getvalue()

    assert output('Egor') == 'Hello, Egor!'
    assert output('Alice') == 'Hello, Alice!'
    assert output('') == 'Hello, !'
