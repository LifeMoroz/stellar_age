class Tech:
    by_tech = ()
    only_for = ()

    def __init__(self, level, tech_lvl=1):
        self.level = level
        self.tech_lvl = tech_lvl

    @property
    def bonus(self):
        return self.by_tech[self.tech_lvl - 1] * self.level
