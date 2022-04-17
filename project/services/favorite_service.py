from project.dao.favorite import FavoriteDAO
from project.services.base import BaseService


class FavoriteService(BaseService):
    def __init__(self, favorite_dao: FavoriteDAO):
        self.favorite_dao = favorite_dao

    def get_favorites_by_user_id(self, user_id):
        return self.favorite_dao.get_favorites_by_user_id(user_id)

    def create(self, data):
        return self.favorite_dao.create(data)

    def delete_movie_from_favorites(self, user_id, movie_id):
        return self.favorite_dao.delete(user_id, movie_id)
