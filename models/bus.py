from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from shemas.bus import Bus
from shemas.park import Park


class Buses(Base):
    __tablename__ = "buses"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    park_id: Mapped[int] = mapped_column(ForeignKey("parks.id"))

    def to_read_model(self) -> Bus:
        return Bus(
            number=self.number,
            park=Park(name="АП-1" if (self.park_id == 1) else "АП-6"),
        )
