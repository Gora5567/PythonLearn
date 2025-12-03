class User:
    def __init__(self):
        self.__password = None

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
