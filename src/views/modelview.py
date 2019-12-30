from flask import request, jsonify, Blueprint
from ..models import db
from ..models.model import Model, ModelSchema

model_api = Blueprint('models', __name__)
model_schema = ModelSchema()
models_schema = ModelSchema(many=True)

# Create model
@model_api.route('', methods=['POST'])
def add_model():
    model_name = request.json['model_name']
    maker_name = request.json['maker_name']
    img_url = request.json['img_url']
    generation_no = request.json['generation_no']
    first_year = request.json['first_year']
    last_year = request.json['last_year']

    new_model = Model(model_name, maker_name, img_url, generation_no,
                      first_year, last_year)

    db.session.add(new_model)
    db.session.commit()

    return jsonify(model_schema.dump(new_model))

# Get all models
@model_api.route('', methods=['GET'])
def get_models():
    all_makers = Model.query.all()
    return jsonify(models_schema.dump(all_makers))

# Get all models from a maker
@model_api.route('/maker/<maker_name>', methods=['GET'])
def get_models_by_maker(maker_name):
    models = Model.query.filter_by(maker_name=maker_name).all()
    return jsonify(models_schema.dump(models))

# Get single model
@model_api.route('/<id>', methods=['GET'])
def get_model(id):
    model = Model.query.get(id)
    return jsonify(model_schema.dump(model))

# Update a model
@model_api.route('/<id>', methods=['PUT'])
def update_model(id):
    model = Model.query.get(id)

    model_name = request.json['model_name']
    maker_name = request.json['maker_name']
    img_url = request.json['img_url']
    generation_no = request.json['generation_no']
    first_year = request.json['first_year']
    last_year = request.json['last_year']

    model.model_name = model_name
    model.maker_name = maker_name
    model.img_url = img_url
    model.generation_no = generation_no
    model.first_year = first_year
    model.last_year = last_year

    db.session.commit()

    return jsonify(model_schema.dump(model))

# Delete model
@model_api.route('/<id>', methods=['DELETE'])
def delete_model(id):
    model = Model.query.get(id)
    db.session.delete(model)
    db.session.commit()
    return jsonify(model_schema.dump(model))
