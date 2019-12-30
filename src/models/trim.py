from . import db
from marshmallow_sqlalchemy import ModelSchema


class Trim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trim_name = db.Column(db.String(30), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'),
                         nullable=False)
    model = db.relationship('Model', backref=db.backref('trims', lazy=True))
    img_url = db.Column(db.String(300))
    vehicule_class = db.Column(db.String(50))
    body_style = db.Column(db.String(100))
    layout = db.Column(db.String(100))
    engine = db.Column(db.String(300))
    transmission = db.Column(db.String(300))

    def __init__(self, trim_name, model_id, img_url, vehicule_class,
                 body_style, layout, engine, transmission):
        self.trim_name = trim_name
        self.model_id = model_id
        self.img_url = img_url
        self.vehicule_class = vehicule_class
        self.body_style = body_style
        self.layout = layout
        self.engine = engine
        self.transmission = transmission


class TrimSchema(ModelSchema):
    class Meta:
        fields = ('id', 'trim_name', 'model_id', 'img_url', 'vehicule_class',
                  'body_style', 'layout', 'engine', 'transmission')
