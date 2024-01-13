from repositories.buses import BusRepository
from services.buses import BusService

"""
Файл внедрения зависимостей
"""
# repository - работа с БД
bus_repository = BusRepository()

# service - слой UseCase
bus_service = BusService(bus_repository)


def get_book_service() -> BusService:
   return bus_service