from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.success_missions = 0
        self.failed_misiions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added"

        astronaut = self.__create_astronaut(astronaut_type, name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added"
        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")
        astrounats = self.astronaut_repository.find_astrounats_for_mission(5, 30)
        if len(astrounats) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        participated_astounat = 0

        for astrounat in astrounats:
            if len(planet.items) == 0:
                break
            while astrounat.oxygen > 0 and len(planet.items) > 0:
                astrounat.backpack.append(planet.items.pop())
                astrounat.breathe()
            participated_astounat += 1

        if len(planet.items) == 0:
            self.success_missions += 1
            return f"Planet: {planet_name} was explored. {participated_astounat} astronauts participated in " \
                   f"collecting items. "
        else:
            self.failed_misiions += 1
            return f"Mission is not completed."

    def report(self):
        result = f"{self.success_missions} successful missions!" + "\n"
        result += f"{self.failed_misiions} missions were not completed!" + "\n"
        result += "Astronauts' info:" + "\n"

        for astro in self.astronaut_repository.astronauts:
            result += str(astro) + "\n"

        return result.strip()

    def __create_astronaut(self, astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)

        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)

        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)

        raise Exception("Astronaut type is not valid!")
