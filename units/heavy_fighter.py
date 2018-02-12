from units.ship import Ship


class HFighter(Ship):
    BASE_ATTACK = 250
    BASE_ARMOR = 1250

    @property
    def priority_attack(self):
        from units.light_fighter import LFighter
        return [LFighter]

    @property
    def avoid(self):
        return []
