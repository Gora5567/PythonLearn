from task9_class_user import User

def test_set_and_get_password():
    u = User()
    u.set_password("secret123")
    assert u.get_password() == "secret123"

def test_empty_password():
    u = User()
    u.set_password("")
    assert u.get_password() == ""
