import base64
import hashlib

from flask import current_app


def generate_password_digest(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=base64.b64decode("salt"),
        iterations=100_000
    )
