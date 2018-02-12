from techs.tech import Tech
from units.cruiser import Cruiser
from units.heavy_fighter import HFighter
from units.light_fighter import LFighter
from units.ship import Ship


class Weapon(Tech):
    def process_ship(self, ship: Ship):
        if not self.only_for or isinstance(ship, self.only_for):
            ship.increase_attack(self.bonus)

    def process_defence(self, ship):
        pass


class Laser(Weapon):
    only_for = (LFighter, HFighter)
    by_tech = (0.01, 0.015, 0.02)


class Gauss(Weapon):
    only_for = (Cruiser,)
    by_tech = (0.01, 0.015, 0.02)


class FleetAttack(Weapon):
    only_for = (Ship,)
    by_tech = (0.01, 0.015, 0.02)

