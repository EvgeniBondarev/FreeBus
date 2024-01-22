from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path

from config import POSTGRES_URI, POSTGRES_ALCHIMY_URL
from depends import get_book_service
from schemas.bus import BusSchema, BusAddSchema, BusEditSchema
from services.bus import BusService

router = APIRouter(prefix="/bus", tags=["Bus"])

@router.get(
"",
    responses={400: {"description": "Bad request"}},
    description="Получение списка всех автобусов.",
    )
async def get_all_bus(bus_service: BusService = Depends(get_book_service)) -> list[BusSchema]:
   buses = await bus_service.get_buses()
   return buses

@router.get(
         "/{number}",
         responses={400: {"description": "Bad request"}},
         description="Получение автобуса по номеру",
    )
async def get_bus_by_number(number: Annotated[int, Path(title="Bus number to change")],
                            bus_service: BusService = Depends(get_book_service)) -> BusSchema:
   bus = await bus_service.get_bus_by_number(number)
   if bus is None:
       raise HTTPException(status_code=404, detail="Item not found")

   return bus

@router.post(
         "",
         responses={400: {"description": "Bad request"}},
         description="Добавления автобуса в БД",
    )
async def add_bus(bus: BusAddSchema, bus_service: BusService = Depends(get_book_service)) -> dict:
   new_id = await bus_service.add_bus(bus)
   return {"new_id": new_id}

@router.patch(
         "/{id}",
         responses={400: {"description": "Bad request"}},
         description="Изменения данных об автобусе по ID",
    )
async def edit_bus(id: Annotated[int, Path(title="ID of the item to be changed")],
                   bus: BusEditSchema, bus_service: BusService = Depends(get_book_service)) -> dict:
   id = await bus_service.edit_bus(id, bus)
   return {"id" : id}

