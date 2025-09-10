from task8_remove_keys import remove_keys


def test_remove_keys_function():
    assert (remove_keys(['name'], name='jack', age=13, city='Odessa') ==
            {'age': 13, 'city': 'Odessa'})
    assert (remove_keys(['age'], name='jack', age=13, city='Odessa') ==
            {'name': "Jack", 'city': 'Odessa'})
    assert (remove_keys(['city'], name='jack', age=13, city='Odessa') ==
            {'name': "Jack", 'age': 13})
а