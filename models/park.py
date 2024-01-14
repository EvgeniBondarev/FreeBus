from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Park(Base):
    __tablename__ = "parks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

