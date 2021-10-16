class Airplane:
    def flyInTheAir(self):
        print('Flying...')


class Ship:
    def floatOnWater(self):
        print('Floating...')


class FlyingBoat(Airplane, Ship):
    pass
