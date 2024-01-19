from typing import List

from models.bus import Buses
from repositories.bus_repository import BusRepository
from schemas.bus import BusAddSchema, BusSchema



class BusService:
    def __init__(self, repository: BusRepository) -> None:
        self.repository = repository

    async def add_bus(self, bus: BusAddSchema) -> None:
        bus_dict = bus.model_dump()
        result = await self.repository.add_one(bus_dict)
        return result

    async def edit_bus(self, id: int, bus: BusSchema):
        bus_dict = bus.model_dump()
        result = await self.repository.edit_one(id, bus_dict)
        return result

    async def get_buses(self) -> List[BusSchema]:
        result = await self.repository.find_all()
        return [res[0].to_api_shema(res[1]) for res in result.all()]

    async def get_bus_by_number(self, number) -> List[BusSchema]:
        filter_condition = Buses.number == number
        result = await self.repository.find_one(filter_condition=filter_condition)
        bus = result.one_or_none()
        return bus[0].to_api_shema(bus[1]) if bus else None



