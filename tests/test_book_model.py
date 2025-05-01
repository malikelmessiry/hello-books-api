from app.models.book import Book
import pytest

def test_from_dict_returns_book():
    book_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    new_book = Book.from_dict(book_data)

    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"

def test_from_dict_with_no_title():
    book_data = {
        "description": "The Best!"
    }

    with pytest.raises(KeyError, match='title'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_no_description():
    book_data = {
        "title": "New Book"
    }

    with pytest.raises(KeyError, match='description'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_extra_keys():
    book_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value" 
    }

    new_book = Book.from_dict(book_data)

    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"