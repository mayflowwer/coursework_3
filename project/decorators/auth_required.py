import jwt
from flask import request, current_app


def auth_required(func):
    def wrapper(self, *args, **kwargs):
        token = request.headers['Authorization'].split(' ')[-1]
        try:
            data = jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=[current_app.config['JWT_ALGORITHM']])
            email = data['email']
        except Exception as e:
            print(e)

        return func(self, email, *args, **kwargs)

    return wrapper
