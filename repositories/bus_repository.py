

from sqlalchemy import select

from db.db import async_session_maker
from models.park import Parks
from utils.repository import SQLAlchemyRepository
from models.bus import Buses

class BusRepository(SQLAlchemyRepository):
    model = Buses
    join_models = [Parks,]

