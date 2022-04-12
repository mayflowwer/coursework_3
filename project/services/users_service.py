from project.dao.user import UserDAO
from project.schemas.user import UserSchema
from project.services.base import BaseService


class UserService(BaseService):
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, user_id: int):
        user = self.user_dao.get_one(user_id)
        return UserSchema.dump(user)

    def get_all(self):
        users = self.user_dao.get_all()
        return UserSchema.dump(users)

    def get_by_email(self, email):
        user = self.user_dao.get_by_email(email)

    def create(self, data: dict):
        return self.user_dao.create(data)

    def update(self, user_id: int, data: dict):
        return self.user_dao.update(user_id, data)

    def delete(self, user_id: int):
        return self.user_dao.delete(user_id)
