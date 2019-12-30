from . import db
from marshmallow_sqlalchemy import ModelSchema


class Equipment(db.Model):
    description = db.Column(db.String(300), primary_key=True)
    trim_name = db.Column(db.String(30),
                          db.ForeignKey('trim.trim_name'),
                          primary_key=True, nullable=False)
    trim = db.relationship('Trim',
                           backref=db.backref('equipments', lazy=True))

    def __init__(self, description, trim_name):
        self.description = description
        self.trim_name = trim_name


class EquipmentSchema(ModelSchema):
    class Meta:
        fields = ('description', 'trim_name')
