from pydantic import BaseModel
from shemas.park import ParkShema


class BusSchema(BaseModel):
    number: int
    park: ParkShema

class BusAddSchema(BaseModel):
    number: int
    park_id: int

class BusEditSchema(BaseModel):
    number: int
    park_id: int