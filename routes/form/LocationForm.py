from pydantic import BaseModel

class CreateLocationBody(BaseModel):
    location_name: str
    description: str

class UpdateLocationBody(BaseModel):
    location_name: str
    description: str

class UpdateLocationNameBody(BaseModel):
    location_name: str

class UpdateLocationDescriptionBody(BaseModel):
    description: str

class LocationPath(BaseModel):
    id: int