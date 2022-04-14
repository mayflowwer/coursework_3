from project.dao.models.base import BaseMixin
from project.setup_db import db


class Genre(BaseMixin, db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"
