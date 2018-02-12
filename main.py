from techs.armor import Armor
from techs.domination import Domination
from techs.weapon import Laser, FleetAttack, Gauss
from units.cruiser import Cruiser
from units.heavy_fighter import HFighter
from units.light_fighter import LFighter


TECH_LIST = [
    Laser(14),
    Laser(6, tech_lvl=2),
    Gauss(1),
    Gauss(5, tech_lvl=2),
    Armor(25),
    Domination(1),
    FleetAttack(17),

]


def get_my_fleet():
    lf = LFighter()
    hf = HFighter()
    for tech in TECH_LIST:
        tech.process_ship(lf)
        tech.process_ship(hf)
    fleet = {
        lf: 100,
        hf: 100
    }
    return fleet


def get_other_fleet():
    hf = HFighter()
    cr = Cruiser()
    for tech in TECH_LIST:
        tech.process_ship(hf)
        tech.process_ship(cr)
    fleet = {
        hf: 100,
        cr: 40
    }
    return fleet


if __name__ == '__main__':
    fleet = get_my_fleet()
    fleet2 = get_other_fleet()
