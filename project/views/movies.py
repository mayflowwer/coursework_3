from flask import request
from flask_restx import Namespace, Resource

from container import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page = request.args.get('page')
        status = request.args.get('status')

        return movie_service.get_all(page=page, status=status)


@movies_ns.route('/<int:user_id>')
class MovieView(Resource):
    def get(self, user_id: int):
        return movie_service.get_one(user_id)
