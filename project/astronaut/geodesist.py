from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    oxygen_geodesist = 50

    def __init__(self, name: str):
        super().__init__(name, self.oxygen_geodesist)

