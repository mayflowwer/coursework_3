from flask import request
from flask_restx import abort, Namespace, Resource

from container import genre_service
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.setup_db import db

genres_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        page = request.args.get('page')
        genres = genre_service.get_all(page=page)
        return genres_schema.dump(genres)


@genres_ns.route("/<int:genre_id>")
class GenreView(Resource):
    def get(self, genre_id: int):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre)
