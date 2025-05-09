from flask import Blueprint, abort, make_response, request, Response
from app.models.genre import Genre
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db
from app.models.book import Book

bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@bp.get("")
def get_genres():
    return get_models_with_filters(Genre, request.args)

@bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)

@bp.post("/<genre_id>/books")
def create_book_with_specific_genre(genre_id):
    genre = validate_model(Genre, genre_id)

    request_body = request.get_json()
    request_body["genres"] = [genre]
    return create_model(Book, request_body)

@bp.get("/<genre_id>/books")
def get_books_by_genre(genre_id):
    genre = validate_model(Genre, genre_id)
    response = [book.to_dict() for book in genre.books]
    return response