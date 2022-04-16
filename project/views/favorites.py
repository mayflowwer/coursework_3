from flask_restx import Namespace, Resource

from container import user_service
from project.decorators.auth_required import auth_required
from project.schemas.favorites import FavoriteSchema

favorites_ns = Namespace('favorites')

favorites_schema = FavoriteSchema(many=True)


@favorites_ns.route('/<int:user_id>')
class FavoriteMoviesView(Resource):
    @auth_required
    def get(self, user_id):
        favorites = user_service.get_favorites_by_user_id(user_id)
        return favorites_schema.dump(favorites)


@favorites_ns.route('/movies/<int:movie_id>')
class FavoriteMovieControl(Resource):
    def post(self, data):
        pass

    def delete(self, movie_id):
        pass
