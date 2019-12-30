from . import db
from marshmallow_sqlalchemy import ModelSchema


class Maker(db.Model):
    maker_name = db.Column(db.String(30), primary_key=True)
    logo_url = db.Column(db.String(200))

    def __init__(self, maker_name, logo_url):
        self.maker_name = maker_name
        self.logo_url = logo_url


class MakerSchema(ModelSchema):
    class Meta:
        fields = ('maker_name', 'logo_url')
