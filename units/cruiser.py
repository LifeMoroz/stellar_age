from units.ship import Ship


class Cruiser(Ship):
    BASE_ATTACK = 950
    BASE_ARMOR = 5000

    @property
    def bonus_eff(self):
        from units.heavy_fighter import HFighter
        return {
            HFighter: 3
        }

    @property
    def priority_attack(self):
        return self.bonus_eff.keys()

    @property
    def avoid(self):
        from units.light_fighter import LFighter
        return [LFighter]
