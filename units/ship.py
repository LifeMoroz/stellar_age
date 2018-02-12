class Ship:
    BASE_ATTACK = 0
    BASE_ARMOR = 0

    def __init__(self):
        self._attack = self.BASE_ATTACK
        self._armor = self.BASE_ARMOR
        self._attack_efficiency = 1
        self._armor_efficiency = 1

    @property
    def priority_attack(self):
        return ()

    @property
    def avoid(self):
        return ()

    @property
    def base_attack(self):
        return self._armor

    @property
    def attack(self):
        return int(self._attack * self._attack_efficiency)

    @property
    def armor(self):
        return int(self._armor * self._armor_efficiency)

    def increase_attack(self, efficiency):
        self._attack_efficiency += efficiency

    def increase_armor(self, efficiency):
        self._armor_efficiency += efficiency
