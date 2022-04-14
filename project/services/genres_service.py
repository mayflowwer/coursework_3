from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenreService(BaseService):
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_one(self, genre_id: int):
        genre = self.genre_dao.get_one(genre_id)
        return genre

    def get_all(self, page=0):
        genres = self.genre_dao.get_all(page=page)
        return genres

    def create(self, data: dict):
        return self.genre_dao.create(data)

    def update(self, genre_id: int, data: dict):
        return self.genre_dao.update(genre_id, data)

    def delete(self, genre_id: int):
        return self.genre_dao.delete(genre_id)
