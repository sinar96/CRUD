from db import database

class Lists(database.Model):
    __tablename__ = 'lists'

    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50))
    age = database.Column(database.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<Lists {}>'.format(self.name)
