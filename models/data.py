from extensions.ext_db import db


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
