from flask import Blueprint, request, jsonify
from services.LocationService import LocationService
from utils.exception import NotFoundError

location_bp = Blueprint('location_bp', __name__)


class LocationForm:
    def __init__(self):
        data = request.get_json()
        self.location_name = data.get('location_name')
        self.description = data.get('description')

@location_bp.route('/locations', methods=['POST'])
def api_create_location():
    try:
        form = LocationForm()
        location = LocationService.create_location(
            form.location_name,
            form.description
        )
        return jsonify({
            'status': 201,
            'data': location.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400

@location_bp.route('/locations', methods=['GET'])
def api_get_all_location():
    location = LocationService.get_all_location()
    return jsonify({
        'status': 200,
        'data': location
    }) if location else ('', 404)

@location_bp.route('/locations/<int:id>', methods=['GET'])
def api_get_location_by_id(id):
    location = LocationService.get_location_by_id(id)
    return jsonify({
        'status': 200,
        'data': location
    }) if location else ('', 404)

@location_bp.route("/locations/<int:id>", methods=["PUT"])
def api_update_location(id):
    try:
        form = LocationForm()
        location = LocationService.update_location(
            id,
            form.location_name,
            form.description,
        )
        return jsonify({
            'message': 'Location updated successfully',
            'status': 201,
            'data': location
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404

@location_bp.route('/locations/<int:id>/location_name', methods=['PATCH'])
def api_update_location_name(id):
    try:
        form = LocationForm()
        location = LocationService.update_location_name(
            id,
            form.location_name
        )
        return jsonify({
            'message': 'Location name updated successfully',
            'status': 201,
            'data': location.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@location_bp.route('/locations/<int:id>/description', methods=['PATCH'])
def api_update_description(id):
    try:
        form = LocationForm()
        location = LocationService.update_description(
            id,
            form.description
        )
        return jsonify({
            'message': 'Location name updated successfully',
            'status': 201,
            'data': location.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@location_bp.route("/locations/<int:id>", methods=["DELETE"])
def api_delete_location(id):
    try:
        LocationService.delete_location(id)
        return jsonify({
            'message': 'Location deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404