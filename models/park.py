from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base
from shemas.park import ParkShema


class Parks(Base):
    __tablename__ = "parks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_api_shema(self) -> ParkShema:
        return ParkShema(
            name=self.name
        )



