from ..guards import cookie_required
from flask import jsonify
from .content import bp

@bp.route('/', methods=['GET'])
@cookie_required
def notifications():
    return jsonify({"message": "Bell created"}), 201

@bp.route('/', methods=['POST'])
@cookie_required
def create_bell():
    return jsonify({"message": "Bell created"}), 201

@bp.route('/', methods=['DELETE'])
@cookie_required
def read_bell():
    return jsonify({"message": "Bell created"}), 201
