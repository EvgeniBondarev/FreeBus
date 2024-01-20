from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from utils.template import templates
from schemas.ticket import TicketSchema
from services.ticket import TicketService
from depends import get_ticket_service


router = APIRouter(prefix="/ticket", tags=["Ticket"])

@router.get(
"/get-ticket",
    responses={400: {"description": "Bad request"}},
    description="Получение билета по номеру автобуса.",
    )
async def get_ticket(bus_number: int,
                     ticket_service: TicketService = Depends(get_ticket_service)) -> TicketSchema:
   result = await ticket_service.get_ticket(bus_number)
   return result


@router.get(
"/get-html-ticket/{bus_number}",
    response_class=HTMLResponse,
    responses={400: {"description": "Bad request"}},
    description="Получение HTML билета по номеру автобуса.",
    )
async def get_html_ticket(request: Request,
                          result=Depends(get_ticket)) -> TicketSchema:
   return templates.TemplateResponse(
       request=request, name="ticket.html", context={
           "bus_number": result.bus.number,
           "park": result.bus.park.name,
           "price": result.price,
           "start_date": result.start_date,
           "end_date": result.end_date,
           "description": result.description
       }
   )

