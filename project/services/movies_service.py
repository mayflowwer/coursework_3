from project.dao.movie import MovieDAO
from project.schemas.movie import MovieSchema
from project.services.base import BaseService


class MovieService(BaseService):
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, movie_id: int):
        movie = self.movie_dao.get_one(movie_id)
        return MovieSchema.dump(movie)

    def get_all(self, page=0, status=None):
        movies = self.movie_dao.get_all(page=page, status=status)
        return MovieSchema.dump(movies)

    def create(self, data: dict):
        return self.movie_dao.create(data)

    def update(self, movie_id: int, data: dict):
        return self.movie_dao.update(movie_id, data)

    def delete(self, movie_id: int):
        return self.movie_dao.delete(movie_id)
