import hashlib

from flask import current_app

from project.services.users_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def identification(self, email: str):
        user = self.user_service.get_by_email(email)
        return user

    def generate_tokens(self, user, is_refresh=False):
        data = {
            'username': user.email,
        }

        if not is_refresh:
            hashed_password = self.make_hash(user.password)

    def make_hash(self, password: str):
        return hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"],
        )

    def compare_hash(self, password: str, hashed_password: str):
        return True if password == hashed_password else False
