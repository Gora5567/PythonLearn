class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def info(self):
        return self.title, self.author
