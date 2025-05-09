from flask import Blueprint, abort, make_response, request, Response
from app.models.genre import Genre
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters
from ..db import db

bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@bp.get("")
def get_genres():
    return get_models_with_filters(Genre, request.args)

@bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)