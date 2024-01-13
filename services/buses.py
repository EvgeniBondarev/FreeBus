from typing import List

from repositories.buses import BusRepository
from shemas.buses import Bus


class BusService:

    def __init__(self, repository: BusRepository) -> None:
        self.repository = repository

    def get_bus(self, bus_number: int) -> List[Bus]:
        result = self.repository.get_bus(bus_number)
        return result

