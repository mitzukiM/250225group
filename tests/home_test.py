class TestBook:
    def test_book(self, book_1):
        assert book_1.inn
        assert book_1.book_author
        assert book_1.title

    def test_inn(self, book_1, book_2):
        assert book_1.inn != book_2.inn


class TestLibrary:
    def test_library(self, library):
        assert library.library_name
        assert library.book_list == []
