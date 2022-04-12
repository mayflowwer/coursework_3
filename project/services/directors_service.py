from project.dao.director import DirectorDAO
from project.schemas.director import DirectorSchema
from project.services.base import BaseService


class DirectorService(BaseService):
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, director_id: int):
        director = self.director_dao.get_one(director_id)
        return DirectorSchema.dump(director_id)

    def get_all(self, page=0):
        directors = self.director_dao.get_all(page=page)
        return DirectorSchema.dump(directors)

    def create(self, data: dict):
        return self.director_dao.create(data)

    def update(self, director_id: int, data: dict):
        return self.director_dao.update(director_id, data)

    def delete(self, director_id: int):
        return self.director_dao.delete(director_id)
