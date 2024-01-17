from typing import List

from fastapi import APIRouter, Depends

from depends import get_book_service
from shemas.bus import Bus
from services.bus import BusService

router = APIRouter(prefix="/bus", tags=["bus"])


@router.get(
         "",
         responses={400: {"description": "Bad request"}},
         #response_model=Bus,
         description="Получение получение данных о заполнении",
    )
async def get_all_bus(book_service: BusService = Depends(get_book_service)) -> dict:
   bus = await book_service.get_bus()
   return {"data" : str(bus)}

@router.get(
         "/{number}",
         responses={400: {"description": "Bad request"}},
         #response_model=Bus,
         description="Получение получение данных о заполнении",
    )
async def get_bus(number: int, book_service: BusService = Depends(get_book_service)) -> dict:
   bus = await book_service.get_bus_by_number(number)
   return {"data" : str(bus)}