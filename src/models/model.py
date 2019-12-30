from . import db
import marshmallow_sqlalchemy


class Model(db.Model):
    model_name = db.Column(db.String(30), primary_key=True)
    maker_name = db.Column(db.String(30), db.ForeignKey('maker.maker_name'),
                           nullable=False)
    maker = db.relationship('Maker', backref=db.backref('models', lazy=True))
    img_url = db.Column(db.String(300))
    generation_no = db.Column(db.Integer)
    first_year = db.Column(db.Integer)
    last_year = db.Column(db.Integer)

    def __init__(self, model_name, maker_name, img_url, generation_no,
                 first_year, last_year):
        self.model_name = model_name
        self.maker_name = maker_name
        self.img_url = img_url
        self.generation_no = generation_no
        self.first_year = first_year
        self.last_year = last_year


class ModelSchema(marshmallow_sqlalchemy.ModelSchema):
    class Meta:
        fields = ('model_name', 'maker_name', 'img_url', 'generation_no',
                  'first_year', 'last_year')
