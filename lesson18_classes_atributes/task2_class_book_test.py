from task2_class_book import Book


def test_book_info():
    b = Book("Dune", "Frank Herbert")
    result = b.info()

    assert result == ("Dune", "Frank Herbert")
