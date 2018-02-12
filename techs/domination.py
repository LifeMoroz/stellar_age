from techs.tech import Tech
from units.ship import Ship


class Domination(Tech):
    by_tech = (0.01, 0.015, 0.02)

    def process_ship(self, ship: Ship):
        ship.increase_armor(self.bonus)
        ship.increase_attack(self.bonus)
