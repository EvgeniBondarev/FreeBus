from pydantic import BaseModel
from schemas.park import ParkSchema


class BusSchema(BaseModel):
    number: int
    park: ParkSchema

class BusAddSchema(BaseModel):
    number: int
    park_id: int

class BusEditSchema(BaseModel):
    number: int
    park_id: int