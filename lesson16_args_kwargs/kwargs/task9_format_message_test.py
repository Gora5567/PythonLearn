from task9_format_message import format_message


def test_format_message():
    assert format_message('Hello, {name}!', name="Egor") == 'Hello, Egor!'
    assert format_message('Hello, {name}!', name="Petro") == 'Hello, Petro!'
    assert format_message('{greet}, name!', greet="Hello") == 'Hello, name!'
