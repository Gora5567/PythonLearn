from task5_class_phone import Phone

def test_phone_attributes():
    p = Phone("Galaxy S24")

    assert Phone.manufacturer == "Apple"
