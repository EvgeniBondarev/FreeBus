from models.bus import Buses
from repositories.bus_repository import BusRepository
from schemas.ticket import TicketSchema
from fastapi import HTTPException
from config import TICKET_CONFIG
from utils.date_manager import generate_dates


class TicketService:
    def __init__(self, repository: BusRepository) -> None:
        self.repository = repository

    async def get_ticket(self, bus_number: int) -> TicketSchema:
        filter_condition = Buses.number == bus_number
        result = await self.repository.find_one(filter_condition=filter_condition)
        bus = result.one_or_none()
        start_date, end_date = generate_dates()

        if bus is None:
            raise HTTPException(status_code=404, detail="Item not found")

        return TicketSchema(bus=bus[0].to_api_shema(bus[1]),
                            price=TICKET_CONFIG.get('price'),
                            description=TICKET_CONFIG.get('description'),
                            start_date=start_date,
                            end_date=end_date
                            )

