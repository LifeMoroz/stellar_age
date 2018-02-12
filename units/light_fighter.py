from units.heavy_fighter import HFighter
from units.ship import Ship
from units.utils import PriorityList


class LFighter(Ship):
    BASE_ATTACK = 100
    BASE_ARMOR = 500

    @property
    def priority_attack(self):
        from units.cruiser import Cruiser
        return PriorityList([Cruiser])

    @property
    def avoid(self):
        return PriorityList([HFighter])
