class Road:
    # Не понял в чем подвох)))
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass_1_sqm = 0
        self.thickness = 0

    def get_mass(self):
        return self._length * self._width * (self.mass_1_sqm / 1000) * (self.thickness * 100)


road = Road(length=5000, width=20)
road.thickness = .05
road.mass_1_sqm = 25
print(road.get_mass())
