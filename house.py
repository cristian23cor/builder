class House:
    def __init__(self):
        self._walls = None
        self._roof = None
        self._windows = None
        self._doors = None

    def set_walls(self, walls):
        self._walls = walls

    def set_roof(self, roof):
        self._roof = roof

    def set_windows(self, windows):
        self._windows = windows

    def set_doors(self, doors):
        self._doors = doors

    def display(self):
        return (f"House with {self._walls} walls, "
                f"{self._roof} roof, "
                f"{self._windows} windows, and "
                f"{self._doors} doors.")
