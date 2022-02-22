from sqlalchemy import Column
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ids=db.Column(db.Integer, unique=True)
    name=db.Column(db.String(100))
    points=db.Column(db.Integer)


