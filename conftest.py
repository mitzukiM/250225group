import pytest

from home_models import Book, Library


@pytest.fixture(scope='class')
def book_1():
    return Book("Taylor Jenkins Reid", "Seven Husbands of Evelyn Hugo")


@pytest.fixture(scope='class')
def book_2():
    return Book(" Holly Jackson", "A Good Girl's Guide to Murder")


@pytest.fixture(scope='class')
def book_3():
    return Book("Mona Awad", "Bunny")


@pytest.fixture(scope='class')
def library():
    return Library("Library named after Taras Shevchenko")


@pytest.fixture(scope='class')
def library_books(library, book_1, book_2, book_3):
    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    return library
