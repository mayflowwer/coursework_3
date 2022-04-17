from project.dao.models.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_favorites_by_user_id(self, user_id):
        return self.session.query(Favorite).filter(Favorite.user_id == user_id).all()

    def create(self, data):
        new_favorite = Favorite(**data)
        self.session.add(new_favorite)
        self.session.commit()

    def delete(self, user_id, movie_id):
        item = self.session.query(Favorite).filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id).first()
        self.session.delete(item)
        self.session.commit()
