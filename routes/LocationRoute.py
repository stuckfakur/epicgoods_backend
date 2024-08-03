from flask import Blueprint, request, jsonify
from services.LocationService import LocationService

location_bp = Blueprint('location_bp', __name__)


class LocationForm:
    def __init__(self):
        data = request.get_json()
        self.location_name = data.get('location_name')
        self.description = data.get('description')


@location_bp.route('/location', methods=['GET'])
def api_get_location():
    location = LocationService.get_all_location()
    return jsonify({
        'status': 200,
        'data': location
    }) if location else ('', 404)

@location_bp.route('/location', methods=['POST'])
def api_create_location():
    form = LocationForm()
    location = LocationService.create_location(
        form.location_name,
        form.description
    )
    return jsonify({
        'status': 201,
        'data': location.to_dict()
    }) if location else ('', 400)