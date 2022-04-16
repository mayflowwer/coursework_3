from flask_restx import abort
from sqlalchemy.exc import IntegrityError

from project.dao.user import UserDAO
from project.schemas.user import UserSchema
from project.services.base import BaseService


class UserService(BaseService):
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, user_id: int):
        user = self.user_dao.get_one(user_id)
        return user

    def get_all(self):
        users = self.user_dao.get_all()
        return users

    def get_by_email(self, email):
        user = self.user_dao.get_by_email(email)
        return user

    def create(self, data: dict):
        try:
            self.user_dao.create(data)
        except IntegrityError as e:
            return e

    def update(self, user_id: int, data: dict):
        return self.user_dao.update(user_id, data)

    def delete(self, user_id: int):
        return self.user_dao.delete(user_id)

    def update_password(self, user_id, password1, password2):
        user = self.user_dao.get_one(user_id)
        old_password = self.make_hash(password1)
        if self.compare_hash(old_password, user.password):
            data = {
                'password': self.make_hash(password2)
            }
            return self.update(user_id, data)
        else:
            abort(400)

    def get_favorites_by_user_id(self, user_id):
        return self.user_dao.get_favorites_by_user_id(user_id)
