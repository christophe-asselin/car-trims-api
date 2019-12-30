from . import db
from marshmallow_sqlalchemy import ModelSchema


class Equipment(db.Model):
    id = db.Colun(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    trim_id = db.Column(db.Integer, db.ForeignKey('trim.id'), nullable=False)
    trim = db.relationship('Trim',
                           backref=db.backref('equipments', lazy=True))

    def __init__(self, description, trim_id):
        self.description = description
        self.trim_id = trim_id


class EquipmentSchema(ModelSchema):
    class Meta:
        fields = ('id', 'description', 'trim_name')
