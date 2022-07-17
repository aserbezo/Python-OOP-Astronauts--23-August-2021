from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Pesho"))
print(space_station.add_astronaut("Geodesist", "Pessho"))
print(space_station.add_astronaut("Biologist", "Pesho"))
print(space_station.add_planet("Mars","Item1 ,Item2"))
print(space_station.send_on_mission("Mars"))
print(space_station.report())
# print(space_station.add_planet("Neptun","tete, ere , erre"))
# print(space_station.add_planet("Neptun","tete, ere , erre"))
#
#
# astrounats = [
# Biologist('Name1'),
# Biologist('Name2'),
# Biologist('Name3'),
# Biologist('Name4'),
# Geodesist('Name5'),
# Geodesist('Name50'),
# Biologist('Name6')
# ]
#
#
# result = sorted([x for x in astrounats if x.oxygen > 50],key=lambda x:x.oxygen,reverse=True)[0:3]
#
# print()