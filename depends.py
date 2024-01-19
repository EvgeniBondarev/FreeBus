from repositories.bus_repository import BusRepository
from services.bus import BusService
from services.ticket import TicketService

bus_repository = BusRepository()


bus_service = BusService(bus_repository)
ticket_service = TicketService(bus_repository)

def get_book_service() -> BusService:
   return bus_service
def get_ticket_service() -> TicketService:
   return ticket_service