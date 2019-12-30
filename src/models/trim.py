from . import db
from marshmallow_sqlalchemy import ModelSchema


class Trim(db.Model):
    trim_name = db.Column(db.String(30), primary_key=True)
    model_name = db.Column(db.String(30), db.ForeignKey('model.model_name'),
                           nullable=False)
    model = db.relationship('Model', backref=db.backref('trims', lazy=True))
    img_url = db.Column(db.String(300))
    vehicule_class = db.Column(db.String(50))
    body_style = db.Column(db.String(100))
    layout = db.Column(db.String(100))
    engine = db.Column(db.String(300))
    transmission = db.Column(db.String(300))

    def __init__(self, trim_name, model_name, img_url, vehicule_class,
                 body_style, layout, engine, transmission):
        self.trim_name = trim_name
        self.model_name = model_name
        self.img_url = img_url
        self.vehicule_class = vehicule_class
        self.body_style = body_style
        self.layout = layout
        self.engine = engine
        self.transmission = transmission


class TrimSchema(ModelSchema):
    class Meta:
        fields = ('trim_name', 'model_name', 'img_url', 'vehicule_class',
                  'body_style', 'layout', 'engine', 'transmission')
