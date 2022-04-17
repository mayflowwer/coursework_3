from flask import request, jsonify
from flask_restx import Namespace, Resource

from container import favorite_service, auth_service
from project.decorators.auth_required import auth_required
from project.schemas.favorites import FavoriteSchema

favorites_ns = Namespace('favorites')

favorites_schema = FavoriteSchema(many=True)


@favorites_ns.route('/<int:user_id>')
class FavoriteMoviesView(Resource):
    @auth_required
    def get(self, user_id):
        favorites = favorite_service.get_favorites_by_user_id(user_id)
        return favorites_schema.dump(favorites)


@favorites_ns.route('/movies/<int:movie_id>')
class FavoriteMovieControl(Resource):
    @auth_required
    def post(self, email, movie_id):
        user = auth_service.identification(email)
        data = {
            'user_id': user.id,
            'movie_id': movie_id
        }
        new_favorite = favorite_service.create(data)

    @auth_required
    def delete(self, email, movie_id):
        user = auth_service.identification(email)
        favorite_service.delete_movie_from_favorites(user.id, movie_id)
