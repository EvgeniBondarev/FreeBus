from typing import List

from shemas.bus import Bus, Park


class BusRepository:

   def get_bus(self, bus_number: int) -> List[Bus]:
       return Bus(number=bus_number, park=Park(name='АП - 2'))