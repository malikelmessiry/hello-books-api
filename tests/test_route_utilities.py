from werkzeug.exceptions import HTTPException
from app.routes.route_utilities import validate_model
from app.models.book import Book
import pytest

def test_validate_book(two_saved_books):
    # act
    # Add `Book` argument to `validate_book` invocation
    result_book = validate_model(Book, 1)

    # assert
    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"

def test_validate_model_missing_record(two_saved_books):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, "3")

    response = error.value.response
    assert response.status == "404 NOT FOUND"
    
def test_validate_model_book_invalid_id(two_saved_books):
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, "cat")

    response = error.value.response
    assert response.status == "400 BAD REQUEST"