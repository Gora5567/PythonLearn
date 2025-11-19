from task20_powers import power_funcs


def test_make_power_funcs():
    funcs = power_funcs()
    results = [f(2) for f in funcs]
    assert results == [1, 2, 4, 8, 16, 32]

    results3 = [f(3) for f in funcs]
    assert results3 == [1, 3, 9, 27, 81, 243]
