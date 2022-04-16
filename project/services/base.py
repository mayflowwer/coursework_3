import hashlib

from flask import current_app
from sqlalchemy.orm.scoping import scoped_session


class BaseService:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def make_hash(self, password: str):
        return hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode("utf-8"),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"],
        )

    def compare_hash(self, password: str, hashed_password: str):
        return True if password == hashed_password else False
