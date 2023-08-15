# Nuestros modelos
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Doll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text, nullable=False)

    __table_args__ = (
        CheckConstraint('price >= 0', name='positive_price'),
    )