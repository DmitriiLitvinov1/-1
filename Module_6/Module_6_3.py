import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        _cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.dz = dz * self.speed
        if self.dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            _cords = self.dx, self.dy, self.dz

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):

        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)}  eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = int(abs(dz * self.speed / 2))
        while self.dz > 0:
            self.dz -= 1


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()
