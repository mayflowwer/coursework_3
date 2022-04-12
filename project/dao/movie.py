from sqlalchemy import desc

from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_all(self, page=0, limit=12, status=None):
        if page == 0 and status is None:
            return self.session.query(Movie).all()
        elif page != 0 and status is None:
            return self.session.query(Movie).offset(page*limit).all()
        elif page != 0 and status == 'new':
            return self.session.query(Movie).order_by(desc(Movie.year)).offset(page*limit).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie_id, data):
        return self.session.query(Movie).filter(Movie.id == movie_id).upate(data)

    def delete(self, movie_id):
        self.session.delete(movie_id)
        self.session.commit()
