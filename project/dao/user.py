from sqlalchemy import desc

from project.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id):
        return self.session.query(User).get(user_id)

    def get_all(self, page=0):
        items_amount = 12
        if page is None:
            return self.session.query(User).all()
        else:
            return self.session.query(User).limit(items_amount).offset(items_amount*(int(page)-1)).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data: dict):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()

    def update(self, user_id, data):
        return self.session.query(User).filter(User.id == user_id).update(data)

    def delete(self, user_id):
        self.session.delete(user_id)
        self.session.commit()
