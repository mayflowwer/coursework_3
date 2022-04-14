from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        return self.session.query(Genre).get(genre_id)

    def get_all(self, page=0):
        items_amount = 12
        if page is None:
            return self.session.query(Genre).all()
        else:
            return self.session.query(Genre).limit(items_amount).offset(items_amount*(int(page)-1)).all()

    def create(self, data):
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()

    def update(self, genre_id, data):
        return self.session.query(Genre).filter(Genre.id == genre_id).upate(data)

    def delete(self, genre_id):
        self.session.delete(genre_id)
        self.session.commit()
