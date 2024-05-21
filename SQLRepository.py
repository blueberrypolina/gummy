from BaseRepository import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    def __init__(self, session):
        self.session = session

    def save(self, data):
        self.session.add(data)
        self.session.commit()

    def find(self, model, query):
        return self.session.query(model).filter_by(**query).first()
