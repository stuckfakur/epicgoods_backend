from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.LocationForm import CreateLocationBody,LocationPath, UpdateLocationBody,UpdateLocationNameBody, UpdateLocationDescriptionBody

from config import Config
from utils.exception import NotFoundError
from services.LocationService import LocationService    

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/locations"
url_prefix = __version__ + __bp__
tag = Tag(name="Location", description="Location API")
location_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)


class LocationForm:
    def __init__(self):
        data = request.get_json()
        self.location_name = data.get('location_name')
        self.description = data.get('description')

@location_bp.post('/create')
@jwt_required()
def api_create_location(body: CreateLocationBody):
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

@location_bp.get('/all')
@jwt_required()
def api_get_all_location():
    location = LocationService.get_all_location()
    return jsonify({
        'status': 200,
        'data': location
    }) if location else ('', 404)

@location_bp.get('/<int:id>')
@jwt_required()
def api_get_location_by_id(path: LocationPath):
    location = LocationService.get_location_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': location
    }) if location else ('', 404)

@location_bp.put('/<int:id>')
@jwt_required()
def api_update_location(path: LocationPath, body: UpdateLocationBody):
    try:
        form = LocationForm()
        location = LocationService.update_location(
            path.id,
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

@location_bp.patch('/<int:id>/location_name')
@jwt_required()
def api_update_location_name(path: LocationPath, body: UpdateLocationNameBody):
    try:
        form = LocationForm()
        location = LocationService.update_location_name(
            path.id,
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

@location_bp.patch('/<int:id>/description')
@jwt_required()
def api_update_description(path: LocationPath, body: UpdateLocationDescriptionBody):
    try:
        form = LocationForm()
        location = LocationService.update_description(
            path.id,
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

@location_bp.delete('/<int:id>')
@jwt_required()
def api_delete_location(path: LocationPath):
    try:
        LocationService.delete_location(path.id)
        return jsonify({
            'message': 'Location deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404