from pydantic import BaseModel


class ParkSchema(BaseModel):
    name: str