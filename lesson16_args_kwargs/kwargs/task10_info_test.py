from task10_info import User


def test_user_creation_with_kwargs():
    user_data = {
        "name": "Egor",
        "email": "egor@gmail.com",
        "age": 13
    }

    # the same as user = User(name="Egor", email="egor@gmail.com", age=13)
    user = User(**user_data)

    assert user.name == "Egor"
    assert user.email == "egor@gmail.com"
    assert user.age == 13

    user.info()
