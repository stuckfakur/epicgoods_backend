from models.Location import Location, db
from sqlalchemy.exc import DataError

class LocationRepository:
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

    @staticmethod
    def get_all_location():
        return Location.query.all()
    
    @staticmethod
    def get_location_by_id(id):
        return Location.query.get(id)

    @staticmethod
    def existing_location_name(location_name, location_id=None):
        existing = Location.query.filter_by(location_name=location_name)
        if location_id:
            existing = existing.filter(Location.id != location_id)

        existing = existing.first()
        return True if existing else False
    
    @staticmethod
    def update_location(id, location_name, description):
        try:
            data = Location.query.get(id)
            if not data:
                return None
            
            data.description = description
            data.updated_at = db.func.now()

            if location_name and location_name != data.location_name:
                if LocationRepository.existing_location_name(location_name, id):
                    raise ValueError('Location name already exists')
                data.location_name = location_name

            db.session.commit()

            return data

        except DataError as e:
            db.session.rollback()
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_location_name(id, location_name):
        try:
            location = Location.query.get(id)
            if not location:
                return None

            location.location_name = location_name
            location.updated_at = db.func.now()

            db.session.commit()

            return location
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def update_description(id, description):
        try:
            location = Location.query.get(id)
            if not location:
                return None

            location.description = description
            location.updated_at = db.func.now()

            db.session.commit()

            return location
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def delete_location(id):
        location = Location.query.get(id)
        if location:
            db.session.delete(location)
            db.session.commit()
        return location