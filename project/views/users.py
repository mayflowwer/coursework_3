from flask import request
from flask_restx import Namespace, Resource

from container import user_service
from project.schemas.user import UserSchema

users_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        page = request.args.get('page')

        users = user_service.get_all(page)
        return users_schema.dump(users)


@users_ns.route('/<int:user_id>')
class UserView(Resource):
    def get(self, user_id: int):
        user = user_service.get_one(user_id)
        return user_schema.dump(user)

    def patch(self, user_id: int):
        data = request.json
        user_service.update(user_id, data)
        return 201


@users_ns.route('<int:user_id>/password')
class UserResetPasswordView(Resource):
    def put(self, user_id: int):
        passwords = request.data
        return passwords
