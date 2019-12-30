from flask import request, jsonify, Blueprint
from ..models import db
from ..models.maker import Maker, MakerSchema


maker_api = Blueprint('makers', __name__)
maker_schema = MakerSchema()
makers_schema = MakerSchema(many=True)

# Create maker
@maker_api.route('', methods=['POST'])
def add_maker():
    maker_name = request.json['maker_name']
    logo_url = request.json['logo_url']

    new_maker = Maker(maker_name, logo_url)

    db.session.add(new_maker)
    db.session.commit()

    return maker_schema.dump(new_maker)

# Get all makers
@maker_api.route('', methods=['GET'])
def get_makers():
    all_makers = Maker.query.all()
    result = makers_schema.dump(all_makers)
    return jsonify(result)

# Get single maker
@maker_api.route('/<maker_name>', methods=['GET'])
def get_maker(maker_name):
    maker = Maker.query.get(maker_name)
    return maker_schema.dump(maker)

# Update a maker
@maker_api.route('/<maker_name>', methods=['PUT'])
def update_maker(maker_name):
    maker = Maker.query.get(maker_name)

    maker_name = request.json['maker_name']
    logo_url = request.json['logo_url']

    maker.maker_name = maker_name
    maker.logo_url = logo_url

    db.session.commit()

    return maker_schema.dump(maker)

# Delete maker
@maker_api.route('/<maker_name>', methods=['DELETE'])
def delete_maker(maker_name):
    maker = Maker.query.get(maker_name)
    db.session.delete(maker)
    db.session.commit()
    return maker_schema.dump(maker)