from project.astronaut.astronaut import Astronaut


class Meteorologist (Astronaut):
    oxygen_meteorologist = 90

    def __init__(self, name: str):
        super().__init__(name, self.oxygen_meteorologist)

    def breathe(self):
        self.oxygen -= 15
