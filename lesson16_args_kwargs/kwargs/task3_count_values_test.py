from task3_count_values import count_values


def test_count_values(**kwargs):
    assert count_values(name='Jack', age=20) == 2
    assert count_values(age=20) == 1
    assert count_values(car='bmw', gender='female', checker='true') == 3
