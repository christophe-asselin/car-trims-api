from flask import request, jsonify, Blueprint
from ..models import db
from ..models.equipment import Equipment, EquipmentSchema


equipment_api = Blueprint('equipment', __name__)
equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)

# Create an equipment
@equipment_api.route('', methods=['POST'])
def add_equipment():
    description = request.json['description']
    trim_id = request.json['trim_id']

    new_equipment = Equipment(description, trim_id)

    db.session.add(new_equipment)
    db.session.commit()

    return jsonify(equipment_schema.dump(new_equipment))

# Get all equipment
@equipment_api.route('', methods=['GET'])
def get_all_equipment():
    all_equipment = Equipment.query.all()
    return jsonify(equipments_schema.dump(all_equipment))

# Get all equipment by trim
@equipment_api.route('/trim/<trim_id>', methods=['GET'])
def get_equipment_by_trim(trim_id):
    equipment = Equipment.query.filter_by(trim_id=trim_id).all()
    return jsonify(equipments_schema.dump(equipment))

# Get single equipment
@equipment_api.route('/<id>', methods=['GET'])
def get_equipment(id):
    equipment = Equipment.query.get(id)
    return jsonify(equipment_schema.dump(equipment))

# Update equipment
@equipment_api.route('/<id>', methods=['PUT'])
def update_equipment(id):
    equipment = Equipment.query.get(id)

    description = request.json['description']
    trim_id = request.json['trim_id']

    equipment.description = description
    equipment.trim_id = trim_id

    db.session.commit()

    return jsonify(equipment_schema.dump(equipment))

# Delete equipment
@equipment_api.route('/<id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = Equipment.query.get(id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify(equipment_schema.dump(equipment))
