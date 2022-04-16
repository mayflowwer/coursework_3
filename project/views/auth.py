from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):  # регистрация пользователя
        email = request.get_json()['email']
        password = request.get_json()['password']

        if 'Authorization' not in request.headers:
            abort(401)

        if email is None:
            abort(404)

        data = {
            'email': email,
            'password': auth_service.make_hash(password)
        }

        user = auth_service.identification(email)

        if user is None:
            new_user = auth_service.user_service.create(data)
        else:
            abort(409)


@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):  # авториазация пользователя
        email = request.get_json()['email']
        password = request.get_json()['password']

        if 'Authorization' not in request.headers:
            abort(401)

        if email is None:
            abort(404)

        data = {
            'email': email,
        }

        user = auth_service.identification(email)

        if user is None:
            abort(401)
        else:
            hashed_password = auth_service.make_hash(password)
            if not auth_service.compare_hash(user.password, hashed_password):
                abort(401)
            else:
                tokens = auth_service.generate_tokens(data)
                return tokens

    def put(self):
        data = request.json
        refresh_tokens = data.get('refresh_token')
        new_tokens = auth_service.get_refresh_tokens(refresh_tokens)
        return new_tokens, 201
