import uuid
from typing import Self

class Book:
    def __init__(self,book_author:str,title:str):
        self.book_author = book_author
        self.title=title
        self.inn: uuid.UUID = uuid.uuid4()
    def __str__(self):
        return f"<Title of the book {self.title} its author {self.book_author} - {self.inn}>"

class Library:
    def __init__(self,library_name:str):
        self.library_name = library_name
        self.book_list = []

    def add_book(self,book):
        self.book_list.append(book)

    def delete_book(self,book_id:uuid.UUID):
        for book in self.book_list:
            if book.book_id == book_id:
                self.book_list.remove(book)
                print(f"Book '{book.title}' removed")
                return
        print("Book with this ID not found.")