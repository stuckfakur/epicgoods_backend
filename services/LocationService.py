from repositories.LocationRepository import LocationRepository

class LocationService:
    @staticmethod
    def get_all_location():
        location = LocationRepository.get_all_location()
        return [location.to_dict() for location in location]
    
    @staticmethod
    def get_location_by_id(id):
        return LocationRepository.get_location_by_id(id)

    @staticmethod
    def create_location(
        location_name,
        description
    ):
        return LocationRepository.create_location(
            location_name,
            description
        )