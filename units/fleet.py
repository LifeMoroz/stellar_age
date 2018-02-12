class Wave:
    def fight(self, fleet1, fleet2):
        for ship, ship_count in fleet1:
            for enemy_ship, enemy_ship_count in fleet2:
                if enemy_ship in ship.priority_attack:
                    ship_attack = ship.attack * ship_count
                    ship_armor = ship.armor * ship_count
                    enemy_attack = enemy_ship.attack * ship_count
                    enemy_armor = enemy_ship.armor * ship_count
                    ship_armor -= enemy_attack
                    enemy_armor -= ship_attack
                    fleet1[ship] = int(ship_armor / ship.armor)
                    fleet2[enemy_ship] = int(enemy_armor / enemy_ship.armor)


class Fleet:
    def __init__(self, fleet):
        self.fleet = fleet.copy()

    def __contains__(self, item):
        for ship in self.fleet:
            if isinstance(ship, item):
                return True
        return False

    def __iter__(self):
        return self.fleet.items()

    def get(self, ship_type):
        for ship in self.fleet:
            if isinstance(ship, ship_type):
                return ship, self.fleet[ship]

    def fight_ships(self):
        pass
