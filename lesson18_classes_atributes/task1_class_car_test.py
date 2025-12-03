from task1_class_car import Car


def test_car_make():
    c = Car("BMW")
    result = c.make()

    assert result == "BMW"
