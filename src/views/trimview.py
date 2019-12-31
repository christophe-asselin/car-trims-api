from flask import request, jsonify, Blueprint
from ..models import db
from ..models.trim import Trim, TrimSchema

trim_api = Blueprint('trims', __name__)
trim_schema = TrimSchema()
trims_schema = TrimSchema(many=True)

# Create trim
@trim_api.route('', methods=['POST'])
def add_trim():
    trim_name = request.json['trim_name']
    model_id = request.json['model_id']
    img_url = request.json['img_url']
    vehicule_class = request.json['vehicule_class']
    body_style = request.json['body_style']
    layout = request.json['layout']
    engine = request.json['engine']
    transmission = request.json['transmission']

    new_trim = Trim(trim_name, model_id, img_url, vehicule_class,
                    body_style, layout, engine, transmission)

    db.session.add(new_trim)
    db.session.commit()

    return jsonify(trim_schema.dump(new_trim))

# Get all trims
@trim_api.route('', methods=['GET'])
def get_trims():
    all_trims = Trim.query.all()
    print(all_trims)
    return jsonify(trims_schema.dump(all_trims))

# Get all trims by model
@trim_api.route('/model/<model_id>', methods=['GET'])
def get_trims_by_model(model_id):
    trims = Trim.query.filter_by(model_id=model_id).all()
    return jsonify(trims_schema.dump(trims))

# Get single trim
@trim_api.route('/<id>', methods=['GET'])
def get_trim(id):
    trim = Trim.query.get(id)
    return jsonify(trim_schema.dump(trim))

# Update a trim
@trim_api.route('/<id>', methods=['PUT'])
def update_trim(id):
    trim = Trim.query.get(id)

    trim_name = request.json['trim_name']
    model_id = request.json['model_id']
    img_url = request.json['img_url']
    vehicule_class = request.json['vehicule_class']
    body_style = request.json['body_style']
    layout = request.json['layout']
    engine = request.json['engine']
    transmission = request.json['transmission']

    trim.trim_name = trim_name
    trim.model_id = model_id
    trim.img_url = img_url
    trim.vehicule_class = vehicule_class
    trim.body_style = body_style
    trim.layout = layout
    trim.engine = engine
    trim.transmission = transmission

    db.session.commit()

    return jsonify(trim_schema.dump(trim))

# Delete trim
@trim_api.route('/<id>', methods=['DELETE'])
def delete_trim(id):
    trim = Trim.query.get(id)
    db.session.delete(trim)
    db.session.commit()
    return jsonify(trim_schema.dump(trim))
