from task8_class_rectangle import Rectangle

def test_area():
    r = Rectangle(5, 3)
    assert r.area() == 15

def test_area_zero():
    r = Rectangle(0, 10)
    assert r.area() == 0
