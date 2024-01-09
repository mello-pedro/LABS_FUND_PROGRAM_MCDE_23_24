# defina aqui a sua classe Círculo
import math
PI = math.pi

class Circle:
    def __init__(self, num):
        self.raio = num
        self.get_area()
        self.get_circumference()

    def get_area(self):
        area = PI * (self.raio ** 2)
        return area

    def get_circumference(self):
        circumference = 2 * PI * self.raio
        return circumference




