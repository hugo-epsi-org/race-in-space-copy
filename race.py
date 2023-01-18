class SpaceShip():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

class Track():
    def __init__(self, length):
        self.length = length
        self.spaceships = []

    def add_spaceship(self, spaceship):
        self.spaceships.append(spaceship)

    def race(self):
        fastest = sorted(self.spaceships, key=lambda spaceship: spaceship.get_speed(), reverse=True)[0]
        return print(f"{fastest.get_name()} l'emporte")

racer1 = SpaceShip('racer1', 2)
racer2 = SpaceShip('racer2', 5)
racer3 = SpaceShip('racer3', 6)
racer4 = SpaceShip('racer4', 8)
racer5 = SpaceShip('racer5', 1)
track1 = Track(1000)

track1.add_spaceship(racer1)
track1.add_spaceship(racer2)
track1.add_spaceship(racer3)
track1.add_spaceship(racer4)
track1.add_spaceship(racer5)
track1.race()