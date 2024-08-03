from models.Location import Location, db

class LocationRepository:
    
    @staticmethod
    def get_all_location():
        return Location.query.all()
    
    @staticmethod
    def get_location_by_id(id):
        return Location.query.get(id)

    @staticmethod
    def create_location(
        location_name,
        description
    ):
       new_location = Location(
           location_name = location_name,
           description = description
       )
       db.session.add(new_location)
       db.session.commit()
       return new_location