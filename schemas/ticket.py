from datetime import datetime, timedelta

from pydantic import BaseModel
from schemas.bus import BusSchema


class TicketSchema(BaseModel):
    bus: BusSchema
    price: float
    start_date: str
    end_date: str
    description: str
