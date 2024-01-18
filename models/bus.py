from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from shemas.bus import BusSchema
from shemas.park import ParkShema


class Buses(Base):
    __tablename__ = "buses"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    park_id: Mapped[int] = mapped_column(ForeignKey("parks.id"))

    def to_api_shema(self, park: ParkShema) -> BusSchema:
        return BusSchema(
            number=self.number if type(self.number) == int else -1,
            park=park.to_api_shema()
        )