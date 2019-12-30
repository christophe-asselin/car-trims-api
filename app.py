from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init ap
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)


class Maker(db.Model):
    maker_name = db.Column(db.String(30), primary_key=True)
    logo_url = db.Column(db.String(200))

    def __init__(self, maker_name, logo_url):
        self.maker_name = maker_name
        self.logo_url = logo_url


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


# Init ma
ma = Marshmallow(app)


class MakerSchema(ma.Schema):
    class Meta:
        fields = ('maker_name', 'logo_url')


class ModelSchema(ma.Schema):
    class Meta:
        fields = ('model_name', 'maker_name', 'img_url', 'generation_no',
                  'first_year', 'last_year')


class TrimSchema(ma.Schema):
    class Meta:
        fields = ('trim_name', 'model_name', 'img_url', 'vehicule_class',
                  'body_style', 'layout', 'engine', 'transmission')


class EquipmentSchema(ma.Schema):
    class Meta:
        fields = ('description', 'trim_name')


maker_schema = MakerSchema()
makers_schema = MakerSchema(many=True)

model_schema = ModelSchema()
models_schema = ModelSchema(many=True)

trim_schema = TrimSchema()
trims_schema = TrimSchema(many=True)

equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)

# Create maker
@app.route('/maker', methods=['POST'])
def add_maker():
    maker_name = request.json['maker_name']
    logo_url = request.json['logo_url']

    new_maker = Maker(maker_name, logo_url)

    db.session.add(new_maker)
    db.session.commit()

    return maker_schema.jsonify(new_maker)


# Get all makers
@app.route('/maker', methods=['GET'])
def get_makers():
    all_makers = Maker.query.all()
    result = makers_schema.dump(all_makers)
    return jsonify(result)


# Get single maker
@app.route('/maker/<maker_name>', methods=['GET'])
def get_maker(maker_name):
    maker = Maker.query.get(maker_name)
    return maker_schema.jsonify(maker)


# Update a maker
@app.route('/maker/<maker_name>', methods=['PUT'])
def update_maker(maker_name):
    maker = Maker.query.get(maker_name)

    maker_name = request.json['maker_name']
    logo_url = request.json['logo_url']

    maker.maker_name = maker_name
    maker.logo_url = logo_url

    db.session.commit()

    return maker_schema.jsonify(maker)


# Delete maker
@app.route('/maker/<maker_name>', methods=['DELETE'])
def delete_maker(maker_name):
    maker = Maker.query.get(maker_name)
    db.session.delete(maker)
    db.session.commit()
    return maker_schema.jsonify(maker)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
