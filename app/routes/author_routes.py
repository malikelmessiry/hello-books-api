from flask import Blueprint, abort, make_response, request, Response
from app.models.author import Author
# from app.models.book import Book
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

# route 1
@bp.post("")
def create_caretaker():
    request_body = request.get_json()

    return create_model(Author, request_body)

    # try:
    #     new_author = Author.from_dict(request_body)
    # except KeyError as error:
    #     response = {"message": f"Invalid request: missing {error.args[0]}"}
    #     abort(make_response(response, 400))

    # db.session.add(new_author)
    # db.session.commit()

    # return new_author.to_dict(), 201

# route 3
@bp.post("/<id>/books")
def create_book_with_author_id(id):
    from app.models.book import Book

    author = validate_model(Author, id)
    request_body = request.get_json()
    request_body["author_id"] = author.id

    return create_model(Book, request_body)

    # try:
    #     new_book = Book.from_dict(request_body)
    # except KeyError as error:
    #     response = {"message": f"Invalid request: missing {error.args[0]}"}
    #     abort(make_response(response, 400))
    
    # db.session.add(new_book)
    # db.session.commit()

    # return new_book.to_dict(), 201

# route 2
@bp.get("")
def get_all_authors():
    return get_models_with_filters(Author, request.args)
    # query = db.select(Author)

    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Author.name.ilike(f"%{name_param}%"))

    # authors = db.session.scalars(query)

    # authors_response = []
    # for author in authors:
    #     authors_response.append(author.to_dict())
    # return authors_response

# route 4
@bp.get("/<id>/books")
def get_all_authors_books(id):
    author = validate_model(Author, id)
    books = [book.to_dict() for book in author.books]

    return books