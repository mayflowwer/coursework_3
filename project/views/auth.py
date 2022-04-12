from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self): # регистрация пользователя
        email = request.get_json()['email']
        password = request.get_json()['password']

        if 'Authorization' not in request.headers:
            abort(401)

        if email is None:
            abort(404)

        data = {
            'email': email,
            'password': password
        }

        user = auth_service.identification(email)

        if user is None:
            new_user = auth_service.user_service.create(data)
            tokens = auth_service.generate_tokens(user, is_refresh=False)
            return tokens


@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self, email, password):

        if 'Authorization' not in request.headers:
            abort(401)

        user = auth_service.identification(email)

        if user:
            hashed_password = auth_service.make_hash(password)
            if auth_service.compare_hash(user.password, hashed_password):
                return auth_service.generate_tokens(user, is_refresh=False)
            else:
                abort(401)

    def put(self):
        data = request.json
        refresh_tokens = data.get('refresh_token')
        new_tokens = auth_service.generate_tokens(is_refresh=True)
        return new_tokens, 201
