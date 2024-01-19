from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.bus import BusSchema
from schemas.park import ParkSchema


class Buses(Base):
    __tablename__ = "buses"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    park_id: Mapped[int] = mapped_column(ForeignKey("parks.id"))

    def to_api_shema(self, park: ParkSchema) -> BusSchema:
        return BusSchema(
            number=self.number if type(self.number) == int else -1,
            park=park.to_api_shema()
        )