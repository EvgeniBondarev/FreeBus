from typing import List

from fastapi import APIRouter, Depends

from depends import get_book_service
from shemas.bus import Bus
from services.buses import BusService

router = APIRouter(prefix="/bus", tags=["bus"])


@router.get(
         "/{bus_number}",
         responses={400: {"description": "Bad request"}},
         response_model=Bus,
         description="Получение получение данных о заполнении",
    )
async def get_all_books(bus_number: int, book_service: BusService = Depends(get_book_service)) -> Bus:
   books = book_service.get_bus(bus_number)
   return books
