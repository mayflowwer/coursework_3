from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from project.schemas.movie import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page = request.args.get('page')
        status = request.args.get('status')

        movies = movie_service.get_all(page, status)
        return movies_schema.dump(movies)

@movies_ns.route('/<int:user_id>')
class MovieView(Resource):
    def get(self, user_id: int):
        movie = movie_service.get_one(user_id)
        return movie_schema.dump(movie)
