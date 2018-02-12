from techs.tech import Tech
from units.ship import Ship


class Armor(Tech):
    EFFICIENCY = 0.01

    def __init__(self, level, tech_lvl=1):
        self.level = level
        if tech_lvl == 1:
            self.efficiency = 0.01 * level
        elif tech_lvl == 2:
            self.efficiency = 0.04 * level
        elif tech_lvl == 3:
            self.efficiency = 0.11 * level
        else:
            raise Exception

    def process_ship(self, ship: Ship):
        ship.increase_armor(self.efficiency)
