from typing import List

from models.bus import Buses
from repositories.bus_repository import BusRepository
from shemas.bus import Bus
from shemas.park import Park


class BusService:
    def __init__(self, repository: BusRepository) -> None:
        self.repository = repository

    async def get_bus(self) -> List[Bus]:
        result = await self.repository.find_all()
        return [(res[0].number, res[1].name) for res in result.all()]

    async def get_bus_by_number(self, number) -> List[Bus]:
        filter_condition = Buses.number == number
        result = await self.repository.find_one(filter_condition=filter_condition)
        return [(res[0].number, res[1].name) for res in result.all()]
