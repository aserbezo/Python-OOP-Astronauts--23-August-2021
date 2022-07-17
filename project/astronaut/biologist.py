from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    oxygen_biologist = 70

    def __init__(self, name: str):
        super().__init__(name, self.oxygen_biologist)

    def breathe(self):
        self.oxygen -= 5

