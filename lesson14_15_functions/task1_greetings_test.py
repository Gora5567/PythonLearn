from task1_greetings import greetings

def test_greetings():
    assert greetings('Egor') == 'Hello, Egor!'
    assert greetings('Alice') == 'Hello, Alice!'
    assert greetings('') == 'Hello, !'
