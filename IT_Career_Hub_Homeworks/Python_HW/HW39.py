import math
from abc import ABC, abstractmethod

class InvalidSizeError(ValueError):
    pass
"""
Create abstract class Shape, and then another two child classes(Rectangle and Circle) that will return the value of area. 
"""
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")