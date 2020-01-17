from . import db
from .trim import TrimSchema
from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import Nested


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    trim_id = db.Column(db.Integer, db.ForeignKey('trim.id'), nullable=False)
    trim = db.relationship('Trim',
                           backref=db.backref('equipments', lazy=True))

    def __init__(self, description, trim_id):
        self.description = description
        self.trim_id = trim_id


class EquipmentSchema(ModelSchema):
    trim = Nested(TrimSchema)

    class Meta:
        model = Equipment
