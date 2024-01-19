from fastapi import APIRouter, Depends

from schemas.ticket import TicketSchema
from services.ticket import TicketService
from depends import get_ticket_service

router = APIRouter(prefix="/ticket", tags=["Ticket"])


@router.get(
"",
    responses={400: {"description": "Bad request"}},
    description="Получение билета по номеру автобуса.",
    )
async def get_ticket(bus_number: int, ticket_service: TicketService = Depends(get_ticket_service)) -> TicketSchema:
   result = await ticket_service.get_ticket(bus_number)
   return result
