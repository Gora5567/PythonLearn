class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.age = kwargs.get('age')

    def info(self):
        buff = self.__dict__

        for name in ["name", "email", "age"]:
            print(f"{name}".format(**buff))
