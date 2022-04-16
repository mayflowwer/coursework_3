import jwt
from flask import request, current_app


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers['Authorization'].split(' ')[-1]
        try:
            jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=[current_app.config['JWT_ALGORITHM']])
        except Exception as e:
            print(e)

        return func(*args, **kwargs)

    return wrapper
