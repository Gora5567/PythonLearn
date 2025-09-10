class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.age = kwargs.get('age')

    def info(self):
        print("\n")

        for k, v in self.__dict__.items():
            print(f"{k}: {v}")

        # for name in ["name", "email", "age"]:
        #     print(f"{name}".format(**self.__dict__))
