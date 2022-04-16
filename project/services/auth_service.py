import calendar
import datetime
import hashlib

import jwt
from flask import current_app
from flask_restx import abort

from project.services.base import BaseService
from project.services.users_service import UserService


class AuthService(BaseService):
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def identification(self, email: str):
        user = self.user_service.get_by_email(email)
        return user

    def generate_tokens(self, data):
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        min30_exp = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, current_app.config["JWT_SECRET"],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        days60 = datetime.datetime.utcnow() + datetime.timedelta(days=60)
        day60_exp = calendar.timegm(days60.timetuple())
        refresh_token = jwt.encode(data, current_app.config["JWT_SECRET"],
                                   algorithm=current_app.config['JWT_ALGORITHM'])

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def get_refresh_tokens(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config["JWT_SECRET"],
                          algorithms=[current_app.config['JWT_ALGORITHM']])
        email = data.get('email')
        user = self.user_service.get_by_email(email)
        data = {
            'email': user.email,
        }
        return self.generate_tokens(data)

    # def make_hash(self, password: str):
    #     return hashlib.pbkdf2_hmac(
    #         hash_name="sha256",
    #         password=password.encode("utf-8"),
    #         salt=current_app.config["PWD_HASH_SALT"],
    #         iterations=current_app.config["PWD_HASH_ITERATIONS"],
    #     )
    #
    # def compare_hash(self, password: str, hashed_password: str):
    #     return True if password == hashed_password else False
