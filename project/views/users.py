from flask import request
from flask_restx import Namespace, Resource

from container import user_service

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        page = request.args.get('page')

        return user_service.get_all(page=page)


@users_ns.route('/<int:user_id>')
class UserView(Resource):
    def get(self, user_id: int):
        return user_service.get_one(user_id)
