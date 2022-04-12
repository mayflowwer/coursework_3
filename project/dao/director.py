from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, director_id):
        return self.session.query(Director).get(director_id)

    def get_all(self, page=0, limit=12):
        if page == 0:
            return self.session.query(Director).all()
        elif page != 0:
            return self.session.query(Director).offset(page*limit).all()

    def create(self, data):
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()

    def update(self, director_id, data):
        return self.session.query(Director).filter(Director.id == director_id).upate(data)

    def delete(self, director_id):
        self.session.delete(director_id)
        self.session.commit()
