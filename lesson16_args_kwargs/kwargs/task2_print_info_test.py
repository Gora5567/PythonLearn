from task2_print_info import print_info

def test_print_info(capsys):
    print_info(name='Jack', age=20)
    out, err = capsys.readouterr()
    assert out == 'name: Jack\nage: 20\n'
