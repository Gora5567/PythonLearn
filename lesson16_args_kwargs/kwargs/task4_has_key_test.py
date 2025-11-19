from task4_has_key import has_key


def test_has_key():
    assert has_key('name', name='Jack', age=20) is True
    assert has_key('Jack', name='Jack', age=20) is False
    assert has_key('age', name='Jack', age=20) is True
