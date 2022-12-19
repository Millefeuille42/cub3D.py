import math


class CubVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, angle):
        old = CubVector(self.x, self.y)
        self.x = old.x * math.cos(math.radians(angle)) - old.y * math.sin(math.radians(angle))
        self.y = old.x * math.sin(math.radians(angle)) + old.y * math.cos(math.radians(angle))
