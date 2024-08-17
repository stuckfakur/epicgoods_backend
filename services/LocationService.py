from repositories.LocationRepository import LocationRepository
from utils.exception import NotFoundError
from sqlalchemy.exc import DataError
import re

class Validator:
    @staticmethod
    def location_validator(location_name, description):
        if not location_name or not isinstance(location_name, str):
            raise ValueError("Location name is required")
        if not description or not isinstance(description, str):
            raise ValueError("description is required")

        regex_Location_name = "^[a-zA-Z\s]+$"
        if not re.match(regex_Location_name, location_name):
            raise ValueError('Please input valid location name')
    
    @staticmethod
    def existing_location_name(location_name):
        if LocationRepository.existing_location_name(location_name):
            raise ValueError('Location name already exist') 

class LocationService:
    @staticmethod
    def create_location(
        location_name,
        description
    ):
        Validator.location_validator(location_name, description)
        Validator.existing_location_name(location_name)
        return LocationRepository.create_location(
            location_name,
            description,
        )
    
    @staticmethod
    def get_all_location():
        location = LocationRepository.get_all_location()
        return [location.to_dict() for location in location]
    
    @staticmethod
    def get_location_by_id(id):
        location = LocationRepository.get_location_by_id(id)
        if location:
            return location.to_dict()
        else:
            return "Location not found"
    
    @staticmethod
    def update_location(locationId, location_name, description):
        Validator.location_validator(location_name, description)
        Validator.existing_location_name(location_name)
        location = LocationService.get_location_by_id(locationId)
        if not location:
            raise NotFoundError("Location not found")
        try:
            location = LocationRepository.update_location(
            locationId,
            location_name,
            description,
            )
            return location.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e

    @staticmethod
    def update_location_name(id, location_name):
        data = LocationService.get_location_by_id(id)
        if not data:
            raise NotFoundError('user not found')

        location = LocationRepository.update_location_name(id, location_name)
        return location  
    
    @staticmethod
    def update_description(id, description):
        data = LocationService.get_location_by_id(id)
        if not data:
            raise NotFoundError('user not found')

        location = LocationRepository.update_description(id, description)
        return location  

    @staticmethod
    def delete_location(id):
        location = LocationRepository.get_location_by_id(id)
        if not location:
            raise NotFoundError("Location not found")
        location = LocationRepository.delete_location(id)
        return location