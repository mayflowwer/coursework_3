from project.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id):
        return self.session.query(User).get(user_id)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data: dict):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()

    def update(self, user_id, data):
        return self.session.query(User).filter(User.id == user_id).update(data)

    def delete(self, user_id):
        self.session.delete(user_id)
        self.session.commit()
