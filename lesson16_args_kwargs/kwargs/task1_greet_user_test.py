from task1_greet_user import greet_user

def test_greet_user():
    assert greet_user(name='Jack', age=20) == 'Hello, Jack!'
    assert greet_user(name='andrei', age=20, gender='female', car='bmw') == 'Hello, andrei!'
    assert greet_user(age=1, gender='female', car='bmw') == 'Hello, guest'