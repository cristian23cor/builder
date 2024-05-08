class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.set_walls(walls)
        return self

    def build_roof(self, roof):
        self.house.set_roof(roof)
        return self

    def build_windows(self, windows):
        self.house.set_windows(windows)
        return self

    def build_doors(self, doors):
        self.house.set_doors(doors)
        return self

    def build(self):
        return self.house
