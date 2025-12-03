from task4_class_cat import Cat


def test_cat_show_name():
    c = Cat("Volt")
    result = c.show_name()

    assert result == "Volt"
