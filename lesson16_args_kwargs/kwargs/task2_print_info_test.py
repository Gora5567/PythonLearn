from task2_print_info import print_info


def test_print_info(**kwargs):
    assert print_info(name='Jack', age=20) == {'name': 'Jack', 'age': 20}
    assert print_info(name='Mike', age=20) == {'name': 'Mike', 'age': 20}
